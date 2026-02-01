import { useEffect, useState, useRef } from "react";
import Sidebar from "../components/Sidebar";
import API from "../api";

export default function Chat() {
  const [chats, setChats] = useState([]);
  const [chatId, setChatId] = useState(null);

  const [messages, setMessages] = useState([]);
  const [question, setQuestion] = useState("");

  const [loading, setLoading] = useState(false);
  const [uploading, setUploading] = useState(false);

  const [url, setUrl] = useState("");

  const fileRef = useRef(null);

  /* =========================
     Load chats
  ========================= */
  useEffect(() => {
    loadChats();
  }, []);

  const loadChats = async () => {
    const res = await API.get("/chat/list");
    setChats(res.data.chats);

    if (res.data.chats.length) {
      selectChat(res.data.chats[0].id);
    }
  };

  /* =========================
     Select chat
  ========================= */
  const selectChat = async (id) => {
    setChatId(id);
    setUrl("");

    const res = await API.get(`/chat/history/${id}`);
    setMessages(res.data.messages || []);
  };

  /* =========================
     Create chat
  ========================= */
  const createChat = async () => {
    const res = await API.post("/chat/new");
    await loadChats();
    selectChat(res.data.chat_id);
  };

  /* ======================================================
     ⭐ STREAMING ASK (FETCH VERSION)
  ====================================================== */
  const ask = async () => {
    if (!question || !chatId) return;

    const token = localStorage.getItem("token");

    const text = question;
    setQuestion("");

    // add user msg
    setMessages((p) => [...p, { role: "user", content: text }]);

    setLoading(true);

    // placeholder assistant msg
    let assistantIndex;

    setMessages((prev) => {
      assistantIndex = prev.length;
      return [...prev, { role: "assistant", content: "" }];
    });

    const res = await fetch("http://127.0.0.1:5000/chat/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        chat_id: chatId,
        question: text,
      }),
    });

    const reader = res.body.getReader();
    const decoder = new TextDecoder();

    let done = false;
    let fullText = "";

    while (!done) {
      const { value, done: doneReading } = await reader.read();
      done = doneReading;

      const chunk = decoder.decode(value || new Uint8Array());
      fullText += chunk;

      // live update
      setMessages((prev) => {
        const updated = [...prev];
        updated[assistantIndex].content = fullText;
        return updated;
      });
    }

    setLoading(false);
  };

  /* =========================
     Upload PDF
  ========================= */
  const uploadPDF = async (file) => {
    if (!file || !chatId) return;

    const fd = new FormData();
    fd.append("file", file);
    fd.append("chat_id", String(chatId));

    setUploading(true);

    try {
      await API.post("/upload/pdf", fd);
      alert("PDF uploaded ✅");
    } catch {
      alert("Upload failed ❌");
    }

    setUploading(false);
  };

  /* =========================
     Upload URL
  ========================= */
  const uploadURL = async () => {
    if (!url || !chatId) return;

    setUploading(true);

    try {
      await API.post("/upload/url", {
        url,
        chat_id: chatId,
      });

      alert("Website added ✅");
      setUrl("");
    } catch {
      alert("URL failed ❌");
    }

    setUploading(false);
  };

  /* =========================
     Logout
  ========================= */
  const logout = () => {
    localStorage.removeItem("token");
    window.location.href = "/login";
  };

  /* =========================
     UI
  ========================= */
  return (
    <div className="flex flex-col md:flex-row h-screen bg-[#0f0f0f] text-white">


    <div className="hidden md:block">
    <Sidebar
    chats={chats}
    activeChat={chatId}
    selectChat={selectChat}
    newChat={createChat}
    logout={logout}
    />
    </div>


      <div className="flex-1 flex flex-col">

        {/* Messages */}
        <div className="flex-1 overflow-y-auto p-6 space-y-6">

          {messages.length === 0 && (
            <div className="text-center text-gray-500 mt-20">
              Upload PDF or Website and ask questions ✨
            </div>
          )}

          {messages.map((m, i) => (
            <div
              key={i}
              className={`max-w-3xl px-4 py-3 rounded-2xl ${
                m.role === "user"
                  ? "bg-blue-600 ml-auto"
                  : "bg-gray-800"
              }`}
            >
              {m.content}
            </div>
          ))}

          {loading && (
            <div className="text-gray-400 animate-pulse">Typing...</div>
          )}
        </div>

        {/* Input bar */}
        {chatId && (
          <div className="border-t border-gray-800 p-4">
            <div className="flex flex-wrap md:flex-nowrap items-center gap-2 bg-gray-900 rounded-2xl px-3 py-2">


              <button onClick={() => fileRef.current.click()}>
                {uploading ? "⏳" : "📎"}
              </button>

              <input
                ref={fileRef}
                type="file"
                hidden
                onChange={(e) => uploadPDF(e.target.files[0])}
              />

              <input
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                placeholder="Website URL..."
                className="bg-gray-800 px-3 py-2 rounded-xl text-sm w-full md:w-56 outline-none"

              />

              <button
                onClick={uploadURL}
                className="bg-purple-600 px-3 py-2 rounded-xl"
              >
                Add
              </button>

              <input
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && ask()}
                placeholder="Ask your document..."
                className="flex-1 bg-transparent outline-none"
              />

              <button
                onClick={ask}
                className="bg-blue-600 px-4 py-2 rounded-xl"
              >
                ➤
              </button>

            </div>
          </div>
        )}
      </div>
    </div>
  );
}

















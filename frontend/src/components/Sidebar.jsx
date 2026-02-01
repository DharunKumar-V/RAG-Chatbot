import { useState } from "react";
import API from "../api";

export default function Sidebar({
  chats,
  activeChat,
  selectChat,
  newChat,
  logout,
}) {
  const [editingId, setEditingId] = useState(null);
  const [title, setTitle] = useState("");

  /* =========================
     Rename chat
  ========================= */
  const renameChat = async (id) => {
    if (!title.trim()) return;

    await API.put(`/chat/rename/${id}`, { title });

    setEditingId(null);
    window.location.reload(); // simple + reliable refresh
  };

  /* =========================
     Delete chat
  ========================= */
  const deleteChat = async (id) => {
    const ok = window.confirm("Delete this chat permanently?");
    if (!ok) return;

    await API.delete(`/chat/delete/${id}`);

    window.location.reload();
  };

  return (
    <div className="w-72 bg-gray-900 border-r border-gray-800 flex flex-col">

      {/* HEADER */}
      <div className="p-4 space-y-3">
        <button
          onClick={newChat}
          className="w-full bg-blue-600 hover:bg-blue-700 py-3 rounded-xl font-semibold"
        >
          + New Chat
        </button>

        <button
          onClick={logout}
          className="w-full bg-gray-800 hover:bg-gray-700 py-2 rounded-xl text-sm"
        >
          Logout
        </button>
      </div>

      {/* CHAT LIST */}
      <div className="flex-1 overflow-y-auto px-3 space-y-2">

        {chats.map((c) => (
          <div
            key={c.id}
            className={`group flex items-center justify-between px-3 py-2 rounded-lg cursor-pointer
              ${
                activeChat === c.id
                  ? "bg-blue-600"
                  : "bg-gray-800 hover:bg-gray-700"
              }`}
            onClick={() => selectChat(c.id)}
          >
            {/* TITLE */}
            {editingId === c.id ? (
              <input
                autoFocus
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                onBlur={() => renameChat(c.id)}
                onKeyDown={(e) => e.key === "Enter" && renameChat(c.id)}
                className="bg-gray-700 px-2 rounded w-full outline-none text-sm"
              />
            ) : (
              <span className="truncate text-sm">
                {c.title || `Chat ${c.id}`}
              </span>
            )}

            {/* ACTIONS (show on hover) */}
            <div className="hidden group-hover:flex gap-2 ml-2 text-xs">

              {/* rename */}
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  setEditingId(c.id);
                  setTitle(c.title || "");
                }}
                className="hover:text-yellow-400"
              >
                ✏️
              </button>

              {/* delete */}
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  deleteChat(c.id);
                }}
                className="hover:text-red-400"
              >
                🗑️
              </button>
            </div>
          </div>
        ))}

      </div>
    </div>
  );
}







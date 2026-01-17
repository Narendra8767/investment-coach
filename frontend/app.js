let sessionId = localStorage.getItem("session_id");

if (!sessionId) {
  newChat();
}

const messages = document.getElementById("messages");

// -------- Load Sidebar Chats --------
async function loadChats() {
  const res = await fetch("/chats");
  const chats = await res.json();

  const list = document.getElementById("chat-list");
  list.innerHTML = "";

  chats.forEach(c => {
    const div = document.createElement("div");
    div.className = "chat-item";
    div.innerText = c.title;
    div.onclick = () => openChat(c.session_id);
    list.appendChild(div);
  });
}

// -------- Open Existing Chat --------
async function openChat(id) {
  sessionId = id;
  localStorage.setItem("session_id", id);

  messages.innerHTML = "";

  const res = await fetch(`/chat/${id}`);
  const history = await res.json();

  history.forEach(m => {
    addMessage(m.role === "user" ? "user" : "bot", m.content);
  });
}

// -------- New Chat --------
function newChat() {
  sessionId = crypto.randomUUID();
  localStorage.setItem("session_id", sessionId);
  messages.innerHTML = "";
  loadChats();
}

// -------- Message Rendering --------
function addMessage(role, text) {
  const div = document.createElement("div");
  div.className = `message ${role}`;

  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.innerText = text;

  div.appendChild(bubble);
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

// -------- Send Message --------
async function send() {
  const input = document.getElementById("input");
  const text = input.value.trim();
  if (!text) return;

  input.value = "";
  addMessage("user", text);
  addMessage("bot", "Thinking…");

  const botBubble = document.querySelector(".bot:last-child .bubble");

  const res = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      message: text,
      session_id: sessionId
    })
  });

  const data = await res.json();
  botBubble.innerText = data.reply;

  loadChats();
}

loadChats();

async function uploadPDF() {
  const input = document.getElementById("pdfInput");

  if (!input) {
    alert("PDF input element not found");
    return;
  }

  input.click();

  input.onchange = async () => {
    const file = input.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch(`/upload-pdf?session_id=${sessionId}`, {
        method: "POST",
        body: formData
      });

      if (!res.ok) {
        throw new Error("Upload failed");
      }

      alert("PDF uploaded successfully");
    } catch (err) {
      alert("PDF upload error");
      console.error(err);
    }

    input.value = ""; // reset
  };
}

---
layout: default
title: Chat with Docs
permalink: /chat/
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.3.0/marked.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/languages/python.min.js"></script>

<div id="chat-container">
  <h2 class="mb-4">📚 QuTiP's Schrödy</h2>
  <div id="messages" class="mb-3"></div>

  <div id="input-group" class="input-group">
    <input
      type="text"
      id="userInput"
      class="form-control"
      placeholder="Type your question..."
      onkeypress="if(event.key === 'Enter') sendMessage()"
    />
    <button class="btn btn-primary" onclick="sendMessage()">Send</button>
  </div>
</div>

<script>
  hljs.highlightAll();

  function appendMessage(role, markdownText) {
    const messagesDiv = document.getElementById("messages");
    const html = marked.parse(markdownText);

    const wrapper = document.createElement("div");
    wrapper.classList.add("message", role);

    const bubble = document.createElement("div");
    bubble.classList.add("bubble");
    bubble.innerHTML = html;

    wrapper.appendChild(bubble);
    messagesDiv.appendChild(wrapper);

    messagesDiv.scrollTop = messagesDiv.scrollHeight;
    hljs.highlightAll(); // Re-highlight after adding new content
  }

  async function sendMessage() {
    const input = document.getElementById("userInput");
    const userText = input.value.trim();
    if (!userText) return;

    appendMessage("user", userText);
    input.value = "";
    input.disabled = true;

    try {
      const resp = await fetch("http://localhost:5001/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText }),
      });

      if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
      const data = await resp.json();

      appendMessage("bot", data.response);
    } catch (err) {
      console.error("Error calling /api/chat:", err);
      appendMessage("bot", "❗ Sorry, something went wrong. Please try again later.");
    } finally {
      input.disabled = false;
      input.focus();
    }
  }

  window.addEventListener("DOMContentLoaded", () => {
    appendMessage(
      "bot",
      `👋 Hi, I'm **Shrody**, QuTiP's doc assistant!  
        I'm here to help you understand and explore the QuTiP documentation.  
        Just ask me a question about how things work—functions, features, usage examples—and I'll do my best to guide you!`
    );
  });
</script>

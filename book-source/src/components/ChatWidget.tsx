import React, { useEffect, useMemo, useRef, useState } from "react";
import "../css/chat.css";

type ChatMessage = {
  id: string;
  role: "user" | "assistant" | "system";
  content: string;
};

const env =
  typeof process !== "undefined" && process.env
    ? process.env
    : ({} as Record<string, string | undefined>);
const API_ORIGIN =
  env.DOCS_CHAT_API_ORIGIN ||
  (typeof window !== "undefined" ? window.location.origin : "http://localhost:8000");
const AUTH_TOKEN = env.DOCS_CHAT_TOKEN || "demo-token";
const SESSION_KEY = "docs-chat-session-id";
const BROWSER_SESSION_KEY = "docs-chat-browser-session-id";

const getBrowserSessionId = () => {
  if (typeof window === "undefined") return null;
  const existing = window.localStorage.getItem(BROWSER_SESSION_KEY);
  if (existing) return existing;
  const generated =
    typeof crypto !== "undefined" && "randomUUID" in crypto
      ? crypto.randomUUID()
      : `browser-${Date.now().toString(16)}-${Math.random().toString(16).slice(2)}`;
  window.localStorage.setItem(BROWSER_SESSION_KEY, generated);
  return generated;
};

export const ChatWidget: React.FC = () => {
  const [open, setOpen] = useState(false);
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [draft, setDraft] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [browserSessionId, setBrowserSessionId] = useState<string | null>(null);
  const messagesEndRef = useRef<HTMLDivElement | null>(null);
  const inputRef = useRef<HTMLInputElement | null>(null);

  const headers = useMemo(() => {
    const base: Record<string, string> = { "Content-Type": "application/json" };
    if (AUTH_TOKEN) {
      base.Authorization = `Bearer ${AUTH_TOKEN}`;
    }
    return base;
  }, []);

  useEffect(() => {
    if (typeof window === "undefined") return;
    const storedSession = window.localStorage.getItem(SESSION_KEY);
    const storedBrowser = getBrowserSessionId();
    if (storedSession) setSessionId(storedSession);
    if (storedBrowser) setBrowserSessionId(storedBrowser);
  }, []);

  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [messages, loading]);

  useEffect(() => {
    if (open && inputRef.current) {
      inputRef.current.focus();
    }
  }, [open]);

  const quickPrompts = [
    "What is robotics?",
    "What is ROS?",
    "How do robots navigate environments?",
    "Explain SLAM in simple terms.",
  ];

  const sendMessage = async () => {
    const text = draft.trim();
    if (!text) return;
    const activeBrowserSession = browserSessionId || getBrowserSessionId();
    if (!activeBrowserSession) {
      setError("Could not establish a browser session.");
      return;
    }
    setBrowserSessionId(activeBrowserSession);
    setMessages((prev) => [...prev, { id: `user-${Date.now()}`, role: "user", content: text }]);
    setDraft("");
    setLoading(true);
    setError(null);

    try {
      const resp = await fetch(`${API_ORIGIN}/chat/query`, {
        method: "POST",
        headers,
        body: JSON.stringify({
          message: text,
          browser_session_id: activeBrowserSession,
          page_url: typeof window !== "undefined" ? window.location.href : undefined,
          session_id: sessionId ?? undefined,
        }),
      });
      if (!resp.ok) {
        throw new Error(`Request failed (${resp.status})`);
      }
      const data = await resp.json();
      if (data.session_id && data.session_id !== sessionId && typeof window !== "undefined") {
        window.localStorage.setItem(SESSION_KEY, data.session_id);
        setSessionId(data.session_id);
      }
      setMessages((prev) => [
        ...prev,
        {
          id: `assistant-${Date.now()}`,
          role: "assistant",
          content: data.answer || "I couldn't find an answer yet.",
        },
      ]);
    } catch (err) {
      console.error(err);
      setError("Could not reach the chat service. Please try again.");
      setMessages((prev) => [
        ...prev,
        { id: `system-${Date.now()}`, role: "system", content: "Something went wrong. Try again soon." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div className="chat-floating-container">
        <button
          className="chat-floating-button"
          aria-label={open ? "Close chat" : "Open chat"}
          aria-expanded={open}
          onClick={() => setOpen((v) => !v)}
        >
          <span className="chat-floating-glow" aria-hidden />
          <span className="chat-floating-icon" aria-hidden>
            {open ? (
              <svg viewBox="0 0 24 24" role="presentation" focusable="false">
                <path
                  d="M7 7l10 10m0-10L7 17"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                />
              </svg>
            ) : (
              <svg viewBox="0 0 24 24" role="presentation" focusable="false">
                <path
                  d="M4.5 4.75C4.5 3.23 5.76 2 7.28 2h9.44C18.24 2 19.5 3.23 19.5 4.75v9.5c0 1.52-1.26 2.75-2.78 2.75H9.6l-3.1 3.22a.75.75 0 0 1-1.27-.53V4.75Z"
                  fill="currentColor"
                />
              </svg>
            )}
          </span>
        </button>
      </div>

      {open && (
        <div className="chat-panel" role="dialog" aria-label="Chat window" aria-modal="false">
          <div className="chat-panel-header">
            <div className="chat-header-meta">
              <div className="chat-status">
                <span className={`chat-status-dot ${sessionId ? "online" : "offline"}`} aria-hidden />
                <span className="chat-title">AI assistant</span>
              </div>
              <div className="chat-subtitle">Ask robotics and ROS questions</div>
            </div>
            <button className="chat-close" onClick={() => setOpen(false)} aria-label="Close chat">
              <svg viewBox="0 0 24 24" role="presentation" focusable="false">
                <path
                  d="M7 7l10 10m0-10L7 17"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                />
              </svg>
            </button>
          </div>

          <div className="chat-prompts" aria-label="Quick prompts">
            {quickPrompts.map((prompt) => (
              <button
                key={prompt}
                className="chat-prompt"
                type="button"
                onClick={() => setDraft(prompt)}
              >
                {prompt}
              </button>
            ))}
          </div>

          <div className="chat-messages" role="log" aria-live="polite">
            {messages.map((m) => (
              <div key={m.id} className={`chat-message chat-${m.role}`}>
                <div className="chat-avatar">
                  {m.role === "user" ? "You" : m.role === "assistant" ? "AI" : "!"}
                </div>
                <div className="chat-bubble">{m.content}</div>
              </div>
            ))}
            {loading && (
              <div className="chat-message chat-assistant">
                <div className="chat-avatar">AI</div>
                <div className="chat-bubble">
                  <div className="chat-typing">
                    <span />
                    <span />
                    <span />
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>
          {error && <div className="chat-error">{error}</div>}
          <div className="chat-input-row">
            <input
              ref={inputRef}
              value={draft}
              onChange={(e) => setDraft(e.target.value)}
              placeholder="Ask anything about robotics or ROS..."
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey) {
                  e.preventDefault();
                  sendMessage();
                }
              }}
            />
            <button onClick={sendMessage} disabled={loading || !draft.trim()}>
              Send
            </button>
          </div>
          <div className="chat-hint">Enter to send · Shift+Enter for newline</div>
        </div>
      )}
    </>
  );
};

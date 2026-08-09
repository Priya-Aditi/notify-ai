import { useEffect, useState } from "react";

import { getMessages } from "./services/api";

import type { Message } from "./types/message";

import MessageCard from "./components/MessageCard";
import AnalyzeMessage from "./components/AnalyzeMessage";


function App() {

  const [messages, setMessages] = useState<Message[]>([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState<string | null>(null);

  const [showAnalyze, setShowAnalyze] = useState(false);


  async function loadMessages() {

    try {

      const data = await getMessages();

      setMessages(data.messages);

    } catch (err) {

      console.error(err);

      setError("Unable to load messages.");

    } finally {

      setLoading(false);

    }
  }


  useEffect(() => {

    loadMessages();

  }, []);


  if (loading) {

    return (
      <div className="loading">
        Loading NotifyAI...
      </div>
    );

  }


  if (error) {

    return (
      <div className="error">
        {error}
      </div>
    );

  }


  return (

    <div className="app">

      {/* Header */}

      <header className="header">

        <div>

          <h1>
            NotifyAI
          </h1>

          <p>
            Your intelligent notification inbox
          </p>

        </div>


        <div className="header-status">
          ● System Healthy
        </div>

      </header>


      {/* Main */}

      <main className="main">

        {/* Sidebar */}

        <aside className="sidebar">

          <button
            className="compose-button"
            onClick={() => setShowAnalyze(true)}
          >
            + Analyze Message
          </button>


          <nav>

            <div className="nav-item active">

              📥 Inbox

              <span>
                {messages.length}
              </span>

            </div>


            <div className="nav-item">

              🔴 Critical

              <span>
                {
                  messages.filter(
                    (message) => message.priority === "P0"
                  ).length
                }
              </span>

            </div>


            <div className="nav-item">

              🟠 High

              <span>
                {
                  messages.filter(
                    (message) => message.priority === "P1"
                  ).length
                }
              </span>

            </div>


            <div className="nav-item">

              🟡 Normal

              <span>
                {
                  messages.filter(
                    (message) => message.priority === "P2"
                  ).length
                }
              </span>

            </div>


            <div className="nav-item">

              ⚪ Low

              <span>
                {
                  messages.filter(
                    (message) => message.priority === "P3"
                  ).length
                }
              </span>

            </div>

          </nav>

        </aside>


        {/* Inbox */}

        <section className="inbox">

          {/* Analyze Message Panel */}

          {showAnalyze && (

            <AnalyzeMessage
              onAnalyzed={() => {

                setShowAnalyze(false);

                loadMessages();

              }}
            />

          )}


          <div className="inbox-header">

            <div>

              <h2>
                Inbox
              </h2>

              <p>
                Messages prioritized by NotifyAI
              </p>

            </div>


            <button className="filter-button">
              All ▾
            </button>

          </div>


          {/* Messages */}

          <div className="message-list">

            {messages.length === 0 ? (

              <div className="empty-state">

                <h3>
                  Your inbox is empty
                </h3>

                <p>
                  Analyze a message to get started.
                </p>

              </div>

            ) : (

              messages.map((message) => (

                <MessageCard
                  key={message.id}
                  message={message}
                />

              ))

            )}

          </div>

        </section>

      </main>

    </div>

  );
}


export default App;
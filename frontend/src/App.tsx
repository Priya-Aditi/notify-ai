function App() {
  return (
    <div className="app">

      {/* Header */}
      <header className="header">
        <div>
          <h1>NotifyAI</h1>
          <p>Your intelligent notification inbox</p>
        </div>

        <div className="header-status">
          ● System Healthy
        </div>
      </header>


      {/* Main content */}
      <main className="main">

        {/* Sidebar */}
        <aside className="sidebar">

          <button className="compose-button">
            + Analyze Message
          </button>

          <nav>
            <div className="nav-item active">
              📥 Inbox
              <span>12</span>
            </div>

            <div className="nav-item">
              🔴 Critical
              <span>2</span>
            </div>

            <div className="nav-item">
              🟠 High
              <span>3</span>
            </div>

            <div className="nav-item">
              🟡 Normal
              <span>5</span>
            </div>

            <div className="nav-item">
              ⚪ Low
              <span>2</span>
            </div>
          </nav>

        </aside>


        {/* Inbox */}
        <section className="inbox">

          <div className="inbox-header">
            <div>
              <h2>Inbox</h2>
              <p>Messages prioritized by NotifyAI</p>
            </div>

            <button className="filter-button">
              All ▾
            </button>
          </div>


          {/* Message list */}
          <div className="message-list">

            <div className="message-card critical">
              <div className="message-indicator"></div>

              <div className="message-content">

                <div className="message-top">
                  <span className="priority-badge critical-badge">
                    Critical
                  </span>

                  <span className="message-time">
                    2 min ago
                  </span>
                </div>

                <h3>
                  Project report due at 4 PM
                </h3>

                <p>
                  Please send the updated project report by 4 PM today.
                </p>

                <div className="message-meta">
                  <span>💼 Work</span>
                  <span>⚡ Action required</span>
                </div>

              </div>
            </div>


            <div className="message-card high">

              <div className="message-indicator"></div>

              <div className="message-content">

                <div className="message-top">
                  <span className="priority-badge high-badge">
                    High
                  </span>

                  <span className="message-time">
                    15 min ago
                  </span>
                </div>

                <h3>
                  Technical interview opportunity
                </h3>

                <p>
                  We'd like to schedule your technical interview.
                  Please share your availability.
                </p>

                <div className="message-meta">
                  <span>💼 Career</span>
                  <span>⚡ Action required</span>
                </div>

              </div>
            </div>


            <div className="message-card normal">

              <div className="message-indicator"></div>

              <div className="message-content">

                <div className="message-top">
                  <span className="priority-badge normal-badge">
                    Normal
                  </span>

                  <span className="message-time">
                    1 hour ago
                  </span>
                </div>

                <h3>
                  Package arriving tomorrow
                </h3>

                <p>
                  Your package has been shipped and will arrive tomorrow.
                </p>

                <div className="message-meta">
                  <span>📦 Delivery</span>
                </div>

              </div>
            </div>


            <div className="message-card low">

              <div className="message-indicator"></div>

              <div className="message-content">

                <div className="message-top">
                  <span className="priority-badge low-badge">
                    Low
                  </span>

                  <span className="message-time">
                    2 hours ago
                  </span>
                </div>

                <h3>
                  Monthly newsletter
                </h3>

                <p>
                  Here are the latest updates and news from our community.
                </p>

                <div className="message-meta">
                  <span>📰 Newsletter</span>
                </div>

              </div>
            </div>

          </div>

        </section>

      </main>

    </div>
  );
}

export default App;
import streamlit as st
import os
from agents.ceo_agent import CEOAgent
from evaluations.evaluator import Evaluator
from database.db_manager import (
    init_db,
    save_startup,
    get_all_startups,
    get_startup_report,
    get_startup_count
)

# ------------------------------------
# Database Initialization
# ------------------------------------

init_db()

# ------------------------------------
# Page Config
# ------------------------------------

st.set_page_config(
    page_title="Agent Forge",
    page_icon="🚀",
    layout="wide"
)

# ------------------------------------
# Sidebar
# ------------------------------------

st.sidebar.title("📚 Startup History")

startup_count = get_startup_count()

st.sidebar.metric(
    "🚀 Startups Generated",
    startup_count
)

history = get_all_startups()

for startup in history:

    startup_id = startup[0]
    startup_idea_history = startup[1]

    if st.sidebar.button(
        f"{startup_id}: {startup_idea_history[:30]}",
        key=f"history_{startup_id}"
    ):

        report = get_startup_report(
            startup_id
        )

        st.header("📄 Saved Startup Report")

        st.markdown(report)

st.sidebar.markdown(
"""
---

## About Agent Forge

AI Startup Factory powered by multi-agent collaboration.

### Features

- CEO Agent
- Multi-Agent Workflow
- SQLite Memory
- Evaluation Dashboard
- Startup History

### Technologies

- Gemini 2.5 Flash
- Streamlit
- SQLite
- Python
"""
)

# ------------------------------------
# Main UI
# ------------------------------------

tab1, tab2 = st.tabs(
    [
        "🚀 Startup Factory",
        "🏗️ Architecture"
    ]
)

# ------------------------------------
# Architecture Tab
# ------------------------------------

with tab2:

    image_path = "assets/agent_architecture.png"

    if os.path.exists(image_path):

        st.image(
            image_path,
            use_container_width=True
        )

    else:

        st.warning(
            "Architecture diagram not found."
        )

# ------------------------------------
# Main App Tab
# ------------------------------------

with tab1:

    st.title(
        "🚀 Agent Forge"
    )
    st.caption(
        "AI Startup Factory powered by multi-agent collaboration"
    )

    st.caption(
        "CEO Agent • Research • Marketing • Investor • Security"
    )


    with st.container(border=True):

        startup_idea = st.text_area(
            "💡 Describe Your Startup Idea",
            placeholder="""
Examples:

• AI SaaS for Dentists
• AI Career Coach for Students
• AI Travel Planner for Families
• AI Personal Finance Assistant
""",
            height=180
        )

        generate = st.button(
            "🚀 Generate Startup Strategy",
            use_container_width=True
        )

    # ------------------------------------
    # Generate Startup
    # ------------------------------------

    if generate:

        if startup_idea:

            with st.spinner(
                "🤖 CEO Agent is coordinating the boardroom..."
            ):
                

                ceo = CEOAgent()

                result = ceo.run(
                    startup_idea
                )

                # ------------------------------------
                # Extract Agent Outputs
                # ------------------------------------

                research = result["research"]
                marketing = result["marketing"]
                investor = result["investor"]
                security = result["security"]
                report = result["report"]

                # ------------------------------------
                # Evaluation
                # ------------------------------------

                evaluation = Evaluator().evaluate(
                    startup_idea,
                    report
                )

                # ------------------------------------
                # Save to SQLite
                # ------------------------------------

                save_startup(
                    startup_idea,
                    report
                )

                # ------------------------------------
                # Agent Status
                # ------------------------------------

                st.success(
                    "🔍 Research Agent completed"
                )

                st.success(
                    "📈 Marketing Agent completed"
                )

                st.success(
                    "💰 Investor Agent completed"
                )

                st.success(
                    "🛡️ Security Agent completed"
                )

                # ------------------------------------
                # Agent Boardroom
                # ------------------------------------

                st.header(
                    "📊 Agent Boardroom"
                )

                with st.expander(
                    "🔍 Research Agent",
                    expanded=False
                ):
                    st.markdown(
                        research
                    )

                with st.expander(
                    "📈 Marketing Agent",
                    expanded=False
                ):
                    st.markdown(
                        marketing
                    )

                with st.expander(
                    "💰 Investor Agent",
                    expanded=False
                ):
                    st.markdown(
                        investor
                    )

                with st.expander(
                    "🛡️ Security Agent",
                    expanded=False
                ):
                    st.markdown(
                        security
                    )

                # ------------------------------------
                # Evaluation Dashboard
                # ------------------------------------

                st.header(
                    "📈 Evaluation Dashboard"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Intent Satisfaction",
                        evaluation[
                            "intent_satisfaction"
                        ]
                    )

                    st.metric(
                        "Feasibility",
                        evaluation[
                            "feasibility"
                        ]
                    )

                with col2:

                    st.metric(
                        "Risk Score",
                        evaluation[
                            "risk_score"
                        ]
                    )

                    st.metric(
                        "Confidence",
                        evaluation[
                            "confidence"
                        ]
                    )

                    st.progress(
                        evaluation[
                            "confidence"
                        ] / 10
                    )

                    if (
                        evaluation[
                            "confidence"
                        ] >= 8
                    ):

                        st.success(
                            "🟢 High Potential Startup"
                        )

                    elif (
                        evaluation[
                            "confidence"
                        ] >= 6
                    ):

                        st.warning(
                            "🟡 Moderate Potential Startup"
                        )

                    else:

                        st.error(
                            "🔴 High Risk Startup"
                        )

                # ------------------------------------
                # Full Report
                # ------------------------------------

                st.header(
                    "📄 Consolidated Startup Report"
                )

                st.markdown(
                    report
                )

                # ------------------------------------
                # Download Report
                # ------------------------------------

                safe_name = (
                    startup_idea
                    .replace(" ", "_")
                    .replace("/", "_")
                )[:30]

                st.download_button(
                    label="📥 Download Startup Report",
                    data=report,
                    file_name=f"{safe_name}_report.md",
                    mime="text/markdown",
                    use_container_width=True
                )

        else:

            st.warning(
                "⚠️ Please enter a startup idea."
            )


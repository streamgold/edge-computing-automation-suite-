#!/usr/bin/env bash
# =========================================================================
# SYSTEM CONTROL INTERFACE: EDGE-COMPUTING DASHBOARD CONTROLLER
# =========================================================================

C_CYAN="\033[1;36m"
C_PURP="\033[1;35m"
C_GREEN="\033[1;32m"
C_YELL="\033[1;33m"
C_WHITE="\033[1;37m"
C_RESET="\033[0m"

while true; do
    clear
    echo -e "${C_CYAN}=========================================================================${C_RESET}"
    echo -e "${C_GREEN} 🌌  MOBILE EDGE-COMPUTING NODE CONTROLLER - MASTER REPO COMMAND DECK   🌌 ${C_RESET}"
    echo -e "${C_CYAN}=========================================================================${C_RESET}"
    echo -e "  1)  ⚡ RUN ACTIVE SCRAPER & DATA ENGINE (Manual Calculation Frame)"
    echo -e "  2)  📄 VIEW LIVE MATRIX TELEMETRY LOGS (Scroll Persistent Dashboard)"
    echo -e "  3)  🧠 RUN 2D DIAGNOSTIC NODE PANEL    (Check Parity & Deltas)"
    echo -e "  4)  🔥 SHOW SIGNAL VELOCITY LEADERBOARD (View Vector Hit Counts)"
    echo -e "  5)  🚀 LAUNCH AUTONOMOUS DAEMON DEPLOY (Power-Saving 1AM Sync Loop)"
    echo -e "  6)  📊 VIEW DATA REVENUE ANALYSIS TOOL (Performance Showdown)"
    echo -e "  7)  📡 VIEW ENVIRONMENTAL FEATURES LOG (Machine & Weather Telemetry)"
    echo -e "  8)  📝 APPEND LATEST METRICS PAYLOAD   (Manual Vector Entry)"
    echo -e "  9)  🤖 TRAIN REINFORCEMENT LEARNING AGENT (Recalculate Q-Table)"
    echo -e "  10) 🧠 INFER ACTIVE REINFORCEMENT POOL  (Agent Policy Outputs)"
    echo -e "  11) 🧬 SYNTHESIZE HYBRID VARIANCE POOL (Core Signal Data Fusion)"
    echo -e "  12) 🧹 PURGE LOCAL WORKSPACE CACHE     (Storage Maintenance)"
    echo -e "  13) 🛑 DISCONNECT CONTROLLER INTERFACE"
    echo -e "${C_CYAN}-------------------------------------------------------------------------${C_RESET}"
    echo -n " 👉 Enter Selection Vector [1-13]: "
    read choice
    echo ""

    case $choice in
        1) if [ -f "./matrix_engine.py" ]; then python3 ./matrix_engine.py; fi; echo -e "\nExecution finished. Press enter..."; read -s ;;
        2) if [ -f "matrix_output.log" ]; then less -R matrix_output.log; else echo -e "\n⚠️ Data log uninitialized."; sleep 1.5; fi ;;
        3) if [ -f "./plot_frequencies.py" ]; then python3 ./plot_frequencies.py; fi; echo -e "\nPress enter to return..."; read -s ;;
        4) echo -e "\n🔥 Velocity tracking offline during background sleep cycles."; sleep 1.5 ;;
        5) echo -e "\n🚀 Spawning Background Autonomous Daemon Schedulers..."; sleep 1.5 ;;
        6) if [ -f "./inspect_matrix.py" ]; then python3 ./inspect_matrix.py; fi; echo -e "\nPress enter to return..."; read -s ;;
        7) if [ -f "./inspect_physics.py" ]; then python3 ./inspect_physics.py; fi; echo -e "\nPress enter to return..."; read -s ;;
        8) if [ -f "./append_physics.py" ]; then python3 ./append_physics.py; fi; echo -e "\nPress enter to return..."; read -s ;;
        9) if [ -f "./rl_agent.py" ]; then python3 ./rl_agent.py; fi; echo -e "\nPress enter to return..."; read -s ;;
        10) if [ -f "./inspect_rl.py" ]; then python3 ./inspect_rl.py; fi; echo -e "\nPress enter to return..."; read -s ;;
        11) if [ -f "./combine_pools.py" ]; then python3 ./combine_pools.py; fi; echo -e "\nPress enter to return..."; read -s ;;
        12) rm -f *.pyc && echo -e "\n🧹 Purged local memory blocks. Framework is pristine."; sleep 1.5 ;;
        13) echo -e "\n👋 Disconnecting console hub vectors safely. Returning to bash.\n"; break ;;
        *) echo -e "\n❌ Invalid entry vector. Press enter to refresh." ; read -s ;;
    esac
done

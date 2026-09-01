#!/usr/bin/env python3
import json, os, csv

def synthesize_hybrid_pool():
    print(f"\033[1;35m🧬 INITIALIZING HYBRID TENSOR INTERSECTION ENGINE...\033[0m")
    print(f"=========================================================================")
    
    macro_pool = [6, 16, 23, 28, 33]
    ai_policy_pool = [24, 28, 30, 31, 34]
    
    q_file = 'rl_q_table.json'
    state_key = "CORE-A_HIGH_PRESSURE"
    ai_scores = {}
    
    if os.path.exists(q_file):
        with open(q_file, 'r') as f:
            q_table = json.load(f)
            if state_key in q_table:
                ai_scores = q_table[state_key]

    candidate_universe = set(macro_pool + ai_policy_pool)
    scored_candidates = {}
    
    for node in candidate_universe:
        synergy_score = 0.0
        
        # Condition 1: Primary Overlap Priority Multiplier
        if node in macro_pool and node in ai_policy_pool:
            synergy_score += 25.0
            
        # Condition 2: AI Action Value Weight Input
        if node in ai_policy_pool:
            synergy_score += float(ai_scores.get(str(node), 12.0))
            
        # Condition 3: Macro-Frequency Baseline Density
        if node in macro_pool:
            synergy_score += 15.0
            
        scored_candidates[node] = round(synergy_score, 4)

    ranked_vectors = sorted(scored_candidates.items(), key=lambda x: x, reverse=True)
    
    print(" 📊 INDIVIDUAL CANDIDATE SYNERGY MATRIX:")
    for node, score in ranked_vectors:
        marker = " [CRITICAL OVERLAP]" if node in macro_pool and node in ai_policy_pool else ""
        print(f"    ▪ Vector ID: #{node:02d} ➔ Synergy Coefficient: {score:<8}{marker}")
        
    final_hybrid_array = [node for node, score in ranked_vectors[:5]]
    final_hybrid_array.sort()
    
    odds = len([x for x in final_hybrid_array if x % 2 != 0])
    evens = len([x for x in final_hybrid_array if x % 2 == 0])
    
    print(f"-------------------------------------------------------------------------")
    print(f" ✨ SYNTHESIZED HYBRID VARIANCE POOL: \033[1;32m{final_hybrid_array}\033[0m")
    print(f" ➔ Geometric Parity Distribution    : {odds} Odds | {evens} Evens (Balanced)")
    print(f"=========================================================================")

if __name__ == "__main__":
    synthesize_hybrid_pool()

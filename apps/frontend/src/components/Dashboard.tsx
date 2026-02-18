import React, { useEffect, useState } from "react";
import { VulnerabilityCard } from "./VulnerabilityCard";
import { PatchSuggestion } from "./PatchSuggestion";
import { AttackGraph } from "./AttackGraph";
import { WebSocketManager } from "../websocket";

export const Dashboard: React.FC = () => {
    const [vulnerabilities, setVulnerabilities] = useState<any[]>([]);
    const [patches, setPatches] = useState<any[]>([]);
    const [graphNodes, setGraphNodes] = useState<any[]>([]);

    useEffect(() => {
        const ws = new WebSocketManager("ws://localhost:8000/ws/updates");
        ws.connect((data: any) => {
            if (data.event === "runtime_scan") setVulnerabilities(data.results);
            if (data.event === "scan_patch") setPatches((prev) => [...prev, data.patch]);
            if (data.event === "attack_graph") setGraphNodes(data.nodes);
        });
    }, []);

    return (
        <div style={{ display: "flex", flexDirection: "column", gap: "20px", padding: "20px" }}>
            <h2>DolanSecOps Dashboard</h2>
            <div>
                <h3>Vulnerabilities</h3>
                {vulnerabilities.map((v, i) => <VulnerabilityCard key={i} vuln={v} />)}
            </div>
            <div>
                <h3>AI Patch Suggestions</h3>
                {patches.map((p, i) => <PatchSuggestion key={i} patch={p} />)}
            </div>
            <div>
                <h3>Attack Graph</h3>
                <AttackGraph nodes={graphNodes} />
            </div>
        </div>
    );
};

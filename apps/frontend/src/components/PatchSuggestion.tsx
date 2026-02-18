import React from "react";

interface PatchProps {
    patch: string;
}

export const PatchSuggestion: React.FC<PatchProps> = ({ patch }) => (
    <div style={{ backgroundColor: "#f0f8ff", padding: "6px", margin: "4px", borderRadius: "6px" }}>
        <pre>{patch}</pre>
    </div>
);

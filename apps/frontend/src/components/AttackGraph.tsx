import React from "react";
import { Graph } from "react-d3-graph";

interface Props {
  data: any[];
}

const AttackGraph: React.FC<Props> = ({ data }) => {
  const graphConfig = {
    nodeHighlightBehavior: true,
    node: { color: "lightblue", size: 300, highlightStrokeColor: "blue" },
    link: { highlightColor: "lightblue" },
    directed: true
  };

  const nodes = data.map(n => ({ id: n.id, label: n.name }));
  const links = data.flatMap(n => n.edges.map(e => ({ source: n.id, target: e.target })));

  return <Graph id="attack-graph" data={{ nodes, links }} config={graphConfig} />;
};

export default AttackGraph;

"use client";

import { Canvas } from "@react-three/fiber";
import { OrbitControls, Text } from "@react-three/drei";

function ProjectNode({
  label,
  position,
}: {
  label: string;
  position: [number, number, number];
}) {
  return (
    <group position={position}>
      <mesh
        onPointerOver={(event) => {
          event.stopPropagation();
          document.body.style.cursor = "pointer";
        }}
        onPointerOut={() => {
          document.body.style.cursor = "default";
        }}
      >
        <boxGeometry args={[2, 1, 2]} />
        <meshStandardMaterial />
      </mesh>

      <Text
        position={[0, 0.7, 0]}
        fontSize={0.35}
        color="white"
        anchorX="center"
        anchorY="middle"
      >
        {label}
      </Text>
    </group>
  );
}

export default function ProjectScene() {
  return (
    <div className="h-[600px] w-full">
      <Canvas camera={{ position: [0, 4, 10], fov: 50 }}>
        <ambientLight intensity={1} />
        <directionalLight position={[5, 8, 5]} intensity={2} />

        <ProjectNode label="Frontend" position={[-3, 1, 0]} />
        <ProjectNode label="Backend" position={[3, 1, 0]} />
        <ProjectNode label="Database" position={[0, 1, -3]} />
        <ProjectNode label="Testing" position={[0, 1, 3]} />

        <OrbitControls />
      </Canvas>
    </div>
  );
}
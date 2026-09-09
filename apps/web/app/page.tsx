import ProjectScene from "@/src/components/ProjectScene";;


export default function Home() {
  return (
    <main className="min-h-screen bg-black text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <h1 className="text-3xl font-semibold">CodeAtlas</h1>

        <p className="mt-2 text-gray-400">
          Explore your codebase visually.
        </p>

        <div className="mt-8 overflow-hidden rounded-2xl border border-white/10">
          <ProjectScene />
        </div>
      </div>
    </main>
  );
}
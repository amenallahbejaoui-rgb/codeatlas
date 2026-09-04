"use client";

import { useState } from "react";

export default function Home() {
  const [url, setUrl] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const isValidGitHubUrl = (value: string) => {
    try {
      const parsed = new URL(value);

      return (
        parsed.hostname === "github.com" &&
        parsed.pathname.split("/").filter(Boolean).length >= 2
      );
    } catch {
      return false;
    }
  };

  const handleAnalyze = async () => {
  setError("");

  if (!url.trim()) {
    setError("Please enter a GitHub repository URL.");
    return;
  }

  if (!isValidGitHubUrl(url.trim())) {
    setError("Please enter a valid GitHub repository URL.");
    return;
  }

  setLoading(true);

  try {
    const response = await fetch("http://localhost:8000/health");

    if (!response.ok) {
      throw new Error("Backend request failed.");
    }

    const data = await response.json();

    console.log("Backend response:", data);
    console.log("Repository URL:", url);
  } catch (error) {
    console.error(error);
    setError("Could not connect to the CodeAtlas backend.");
  } finally {
    setLoading(false);
  }
};

  return (
    <main className="min-h-screen flex items-center justify-center px-6">
      <div className="w-full max-w-3xl text-center">
        <div className="mb-8">
          <span className="text-sm font-medium text-zinc-400">
            CodeAtlas
          </span>
        </div>

        <h1 className="text-5xl font-bold tracking-tight sm:text-6xl">
          Understand any codebase.
        </h1>

        <p className="mx-auto mt-6 max-w-2xl text-lg text-zinc-400">
          Turn a GitHub repository into a simple visual architecture map.
          See the frontend, backend, database, cloud, and CI/CD at a glance.
        </p>

        <div className="mx-auto mt-10 flex max-w-2xl flex-col gap-3 sm:flex-row">
          <input
            type="url"
            value={url}
            onChange={(event) => {
              setUrl(event.target.value);
              setError("");
            }}
            placeholder="https://github.com/user/project"
            className="h-14 flex-1 rounded-xl border border-zinc-800 bg-zinc-900 px-5 text-sm text-white outline-none placeholder:text-zinc-600 focus:border-zinc-600"
          />

          <button
            onClick={handleAnalyze}
            disabled={loading}
            className="h-14 rounded-xl bg-white px-7 text-sm font-semibold text-black transition hover:bg-zinc-200 disabled:cursor-not-allowed disabled:opacity-50"
          >
            {loading ? "Analyzing..." : "Analyze →"}
          </button>
        </div>

        {error && (
          <p className="mt-4 text-sm text-red-400">
            {error}
          </p>
        )}

        <p className="mt-5 text-sm text-zinc-600">
          No signup required
        </p>
      </div>
    </main>
  );
}
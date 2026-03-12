"use client";

import React from "react";

export default function Hero({ onSearch }) {
  const [query, setQuery] = React.useState("");

  const handleSearch = () => {
    if (onSearch) {
      onSearch(query);
    }
  };

  const handleCallEmergency = () => {
    window.location.href = "tel:911";
  };

  const handleStartGuidedAid = () => {
    // Scroll down smoothly to the guide library section
    const guideSection = document.getElementById("guide-library");
    if (guideSection) {
      guideSection.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <div className="px-6 py-6 max-w-5xl mx-auto">

      {/* HERO CARD */}
      <div className="bg-white shadow-md rounded-xl p-6 flex flex-col md:flex-row items-center justify-between">
        <div className="flex-1">
          <h2 className="text-2xl font-bold text-gray-800">
            First aid guidance when it matters
          </h2>

          <p className="text-gray-600 mt-2">
            Quick, localised, offline-capable instructions and mental wellness support
            tailored to Uganda & East Africa.
          </p>

          <div className="flex space-x-3 mt-4 flex-wrap gap-y-2">
            <a
              href="tel:911"
              className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700 transition font-semibold flex items-center gap-2"
            >
              📞 Call 911
            </a>

            <button
              onClick={handleStartGuidedAid}
              className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition font-semibold flex items-center gap-2"
            >
              🩺 Start Guided Aid
            </button>
          </div>
        </div>

        <div className="mt-6 md:mt-0 text-center">
          <div className="text-green-600 text-7xl font-light">+</div>
          <p className="text-gray-500 text-xs">
            Offline-ready guides & local<br /> language support
          </p>
        </div>
      </div>

      {/* SEARCH BAR */}
      <div className="mt-6">
        <form
          onSubmit={(e) => {
            e.preventDefault();
            handleSearch();
          }}
          className="bg-white shadow-md rounded-xl p-3 flex items-center"
        >
          <input
            type="text"
            placeholder="Search first aid guides (e.g., bleeding, burn)"
            className="flex-1 px-3 py-2 outline-none text-gray-700"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <button
            type="submit"
            className="ml-3 bg-green-600 text-white px-6 py-2 rounded-lg font-semibold hover:bg-green-700 transition"
          >
            Search
          </button>
        </form>
      </div>

    </div>
  );
}

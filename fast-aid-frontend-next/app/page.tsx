"use client";

import React, { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import Hero from "@/components/Hero";
import GuideCard from "@/components/GuideCard";
import axios from "axios";

export default function Home() {
  const router = useRouter();
  const [guides, setGuides] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState("");
  const [noResults, setNoResults] = useState(false);

  const fetchGuides = (query = "") => {
    setLoading(true);
    setNoResults(false);
    axios
      .get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/guides/search?q=${encodeURIComponent(query)}`)
      .then((res) => {
        const items = res.data.items || [];
        // If exactly 1 result, redirect directly to that guide
        if (query.trim() && items.length === 1) {
          router.push(`/guide/${items[0].id}`);
          return;
        }
        setGuides(items);
        setNoResults(items.length === 0 && query.trim() !== "");
        setLoading(false);
      })
      .catch((err) => {
        console.error("Failed to fetch guides:", err);
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchGuides();
  }, []);

  const handleSearch = (query: string) => {
    setSearchQuery(query);
    fetchGuides(query);
  };

  return (
    <div className="flex flex-col gap-12 pb-12">
      <Hero onSearch={handleSearch} />

      {/* GUIDE CARDS */}
      <section id="guide-library" className="container mx-auto px-6">
        <div className="flex items-center justify-between mb-8">
          <div>
            <h2 className="text-3xl font-bold text-gray-800">First Aid Guides</h2>
            {searchQuery && (
              <p className="text-sm text-gray-500 mt-1">
                Showing results for <span className="font-semibold text-green-600">"{searchQuery}"</span>
                <button
                  onClick={() => { setSearchQuery(""); fetchGuides(""); }}
                  className="ml-2 text-red-500 underline text-xs hover:text-red-700"
                >
                  Clear
                </button>
              </p>
            )}
          </div>
          <div className="h-1 flex-1 bg-green-100 mx-6 rounded-full hidden md:block"></div>
        </div>

        {loading ? (
          <div className="flex justify-center py-12">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-green-600"></div>
          </div>
        ) : noResults ? (
          <div className="bg-white rounded-xl shadow-sm p-12 text-center">
            <div className="text-5xl mb-4">🔍</div>
            <p className="text-gray-700 text-lg font-semibold">No guides found for "{searchQuery}"</p>
            <p className="text-gray-500 mt-2">Try a different keyword like "burn", "choking", or "fracture".</p>
            <button
              onClick={() => { setSearchQuery(""); fetchGuides(""); }}
              className="mt-6 bg-green-600 text-white px-6 py-2 rounded-lg hover:bg-green-700 transition"
            >
              View All Guides
            </button>
          </div>
        ) : guides.length > 0 ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {guides.map((g) => (
              <GuideCard
                key={g.id}
                id={g.id}
                title={g.title}
                time={g.estimated_time}
                summary={g.summary}
                tags={[g.category]}
              />
            ))}
          </div>
        ) : (
          <div className="bg-white rounded-xl shadow-sm p-12 text-center">
            <p className="text-gray-500 text-lg">No guides available at the moment. Please check back later.</p>
          </div>
        )}
      </section>

      {/* EMERGENCY CONTACTS QUICK LINK */}
      <section className="container mx-auto px-6">
        <div className="bg-red-50 border border-red-100 rounded-2xl p-8 flex flex-col md:flex-row items-center justify-between gap-6">
          <div>
            <h3 className="text-2xl font-bold text-red-700 mb-2">Emergency?</h3>
            <p className="text-red-600">Quickly find the help you need or call for an ambulance immediately.</p>
          </div>
          <div className="flex gap-4 flex-wrap">
            <a
              href="tel:911"
              className="bg-red-600 text-white px-8 py-3 rounded-xl font-bold hover:bg-red-700 transition shadow-lg shadow-red-200 flex items-center gap-2"
            >
              📞 Call 911
            </a>
            <button
              onClick={() => {
                if (navigator.geolocation) {
                  navigator.geolocation.getCurrentPosition(
                    (pos) => {
                      const { latitude, longitude } = pos.coords;
                      const mapsUrl = `https://www.google.com/maps/search/clinic+near+me/@${latitude},${longitude},14z`;
                      window.open(mapsUrl, "_blank");
                    },
                    () => {
                      // Fallback: open Google Maps without GPS
                      window.open("https://www.google.com/maps/search/clinic+near+me", "_blank");
                    }
                  );
                } else {
                  window.open("https://www.google.com/maps/search/clinic+near+me", "_blank");
                }
              }}
              className="bg-white text-red-600 border-2 border-red-600 px-8 py-3 rounded-xl font-bold hover:bg-red-50 transition flex items-center gap-2"
            >
              📍 Find Clinics Near Me
            </button>
          </div>
        </div>
      </section>
    </div>
  );
}

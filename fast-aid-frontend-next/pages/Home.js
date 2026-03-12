import React, { useEffect, useState } from "react";
import Hero from "../components/Hero";
import GuideCard from "../components/GuideCard";
import Footer from "../components/Footer";
import axios from "axios";

const Home = () => {
  const [guides, setGuides] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/guides/search?q=")
      .then((res) => {
        // Backend returns {page, page_size, total, items: []}
        setGuides(res.data.items || []);
      })
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="flex flex-col gap-16">

      <Hero />

      {/* SEARCH BAR */}
      <section className="container mx-auto px-6">
        <h2 className="text-2xl font-bold mb-4">Search for Help</h2>

        <div className="bg-white shadow-md rounded-xl p-3 flex items-center">
          <input
            type="text"
            placeholder="Search first aid guides (e.g., bleeding, burn)"
            className="flex-1 px-3 py-2 outline-none text-gray-700"
          />

          <button className="ml-3 text-gray-500 hover:text-gray-700">
            Search...
          </button>
        </div>
      </section>

      {/* GUIDE CARDS */}
      <section className="container mx-auto px-6">
        <h2 className="text-2xl font-bold mb-4">Quick Guides</h2>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {guides.length > 0 ? (
            guides.slice(0, 6).map((g) => (
              <GuideCard
                key={g.id}
                id={g.id}
                title={g.title}
                time={g.estimated_time}
                summary={g.summary}
                tags={[g.category, g.urgency]}
              />
            ))
          ) : (
            <p>No guides available.</p>
          )}
        </div>
      </section>

      {/* COMMON GUIDE SECTION */}
      <section className="container mx-auto px-6 mt-4">
        <h2 className="text-2xl font-bold mb-4">Common guides</h2>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {guides.slice(6, 9).map((g) => (
            <GuideCard
              key={g.id}
              id={g.id}
              title={g.title}
              time={g.estimated_time}
              summary={g.summary}
              tags={[g.category, g.urgency]}
            />
          ))}
        </div>
      </section>

      <Footer />
    </div>
  );
};

export default Home;

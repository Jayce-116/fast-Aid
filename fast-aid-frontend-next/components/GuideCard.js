import React from "react";
import Link from "next/link";

const GuideCard = ({ id, title, time, summary, tags }) => {
  return (
    <div className="bg-white rounded-xl shadow p-6 flex flex-col hover:shadow-lg transition-shadow">
      <h3 className="text-xl font-bold mb-2 text-gray-800">{title}</h3>
      <p className="text-gray-500 text-sm mb-2">{time}</p>
      <p className="text-gray-700 mb-4 line-clamp-3">{summary}</p>

      <div className="flex flex-wrap gap-2 mb-4">
        {tags && tags.filter(Boolean).map((tag, index) => (
          <span
            key={index}
            className="bg-green-100 px-3 py-1 rounded-full text-xs text-green-700 font-medium"
          >
            {tag}
          </span>
        ))}
      </div>

      <Link
        href={`/guide/${id}`}
        className="inline-block bg-green-600 text-white text-center py-2 rounded font-semibold hover:bg-green-700 transition mt-auto"
      >
        Open Guide
      </Link>
    </div>
  );
};

export default GuideCard;


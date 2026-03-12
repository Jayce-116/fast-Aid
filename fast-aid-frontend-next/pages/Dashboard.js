import React, { useEffect, useState } from "react";

export default function Dashboard() {
  const [username, setUsername] = useState("");

  useEffect(() => {
    const user = localStorage.getItem("username");
    if (user) setUsername(user);
  }, []);

  return (
    <div className="p-6 md:p-10 bg-gray-50 min-h-screen">

      {/* Welcome Section */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-800">
          Welcome{username ? `, ${username}` : ""} 
        </h1>
        <p className="text-gray-600 mt-2">
          Your personalized first aid & wellness dashboard
        </p>
      </div>

      {/* Quick Actions */}
      <div className="grid md:grid-cols-3 gap-6">

        {/* Guided Aid */}
        <div className="p-6 bg-white rounded-2xl shadow hover:shadow-lg transition">
          <h2 className="text-xl font-semibold mb-3 text-gray-800">
            Guided First Aid
          </h2>
          <p className="text-gray-600 mb-4">
            Step-by-step instructions tailored to the emergency.
          </p>
          <button className="bg-green-600 text-white px-4 py-2 rounded">
            Start Guided Aid
          </button>
        </div>

        {/* Browse Guides */}
        <div className="p-6 bg-white rounded-2xl shadow hover:shadow-lg transition">
          <h2 className="text-xl font-semibold mb-3 text-gray-800">
            Browse First Aid Guides
          </h2>
          <p className="text-gray-600 mb-4">
            Access life-saving instructions for common emergencies.
          </p>
          <button className="bg-blue-600 text-white px-4 py-2 rounded">
            View Guides
          </button>
        </div>

        {/* Emergency */}
        <div className="p-6 bg-white rounded-2xl shadow hover:shadow-lg transition">
          <h2 className="text-xl font-semibold mb-3 text-gray-800">
            Emergency Call
          </h2>
          <p className="text-gray-600 mb-4">
            Quickly call emergency services when you need urgent help.
          </p>
          <button className="bg-red-600 text-white px-4 py-2 rounded">
            Call Emergency
          </button>
        </div>
      </div>

      {/* Wellness Tips */}
      <div className="mt-10 p-6 bg-white rounded-2xl shadow">
        <h2 className="text-xl font-semibold text-gray-800 mb-3">
          Wellness Tip of the Day 
        </h2>
        <p className="text-gray-600">
          Drinking water regularly keeps your body and mind alert. Stay hydrated!
        </p>
      </div>

    </div>
  );
}

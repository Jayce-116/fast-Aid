"use client";

import React, { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export default function DashboardPage() {
  const [username, setUsername] = useState("");
  const router = useRouter();

  useEffect(() => {
    const user = localStorage.getItem("username");
    const token = localStorage.getItem("token");
    
    if (!token) {
      router.push("/login");
      return;
    }
    
    if (user) setUsername(user);
  }, [router]);

  return (
    <div className="p-6 md:p-10 bg-gray-50 min-h-screen">
      {/* Welcome Section */}
      <div className="mb-12">
        <h1 className="text-4xl font-extrabold text-gray-900 tracking-tight">
          Welcome back{username ? `, ${username}` : ""}!
        </h1>
        <p className="text-lg text-gray-500 mt-2">
          Your personalized first aid & wellness dashboard
        </p>
      </div>

      {/* Quick Actions */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        {/* Guided Aid */}
        <div className="group p-8 bg-white rounded-3xl shadow-sm border border-gray-100 hover:shadow-xl hover:border-green-100 transition-all duration-300">
          <div className="w-12 h-12 bg-green-100 rounded-2xl flex items-center justify-center text-green-600 mb-6 group-hover:scale-110 transition-transform">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m16 6 4 14-8-8-8 8 4-14 4 4 4-4Z"/></svg>
          </div>
          <h2 className="text-2xl font-bold mb-3 text-gray-800">
            Guided First Aid
          </h2>
          <p className="text-gray-600 mb-8 leading-relaxed">
            Step-by-step instructions tailored to the specific emergency you are facing.
          </p>
          <button className="w-full bg-green-600 text-white font-bold py-3 rounded-2xl hover:bg-green-700 transition shadow-lg shadow-green-50">
            Start Guided Aid
          </button>
        </div>

        {/* Browse Guides */}
        <div className="group p-8 bg-white rounded-3xl shadow-sm border border-gray-100 hover:shadow-xl hover:border-blue-100 transition-all duration-300">
          <div className="w-12 h-12 bg-blue-100 rounded-2xl flex items-center justify-center text-blue-600 mb-6 group-hover:scale-110 transition-transform">
             <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"/><path d="M8 7h6"/><path d="M8 11h8"/></svg>
          </div>
          <h2 className="text-2xl font-bold mb-3 text-gray-800">
            Browse Guides
          </h2>
          <p className="text-gray-600 mb-8 leading-relaxed">
            Access our full library of life-saving instructions for common medical situations.
          </p>
          <button className="w-full bg-blue-600 text-white font-bold py-3 rounded-2xl hover:bg-blue-700 transition shadow-lg shadow-blue-50" onClick={() => router.push("/")}>
            View Library
          </button>
        </div>

        {/* Emergency */}
        <div className="group p-8 bg-white rounded-3xl shadow-sm border border-gray-100 hover:shadow-xl hover:border-red-100 transition-all duration-300">
          <div className="w-12 h-12 bg-red-100 rounded-2xl flex items-center justify-center text-red-600 mb-6 group-hover:scale-110 transition-transform">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          </div>
          <h2 className="text-2xl font-bold mb-3 text-gray-800">
            Emergency Help
          </h2>
          <p className="text-gray-600 mb-8 leading-relaxed">
            Quick access to emergency services and local ambulance contacts in your area.
          </p>
          <button className="w-full bg-red-600 text-white font-bold py-3 rounded-2xl hover:bg-red-700 transition shadow-lg shadow-red-50">
            Panic Button
          </button>
        </div>
      </div>

      {/* Wellness Tips */}
      <div className="mt-12 p-10 bg-gradient-to-r from-green-600 to-green-500 rounded-3xl shadow-xl text-white">
        <div className="flex items-center gap-4 mb-4">
          <div className="p-2 bg-white/20 rounded-full">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/></svg>
          </div>
          <h2 className="text-2xl font-bold">
            Wellness Tip of the Day 
          </h2>
        </div>
        <p className="text-xl opacity-90 leading-relaxed font-medium">
          "Drinking water regularly keeps your body and mind alert. Stay hydrated specifically during hot days to maintain optimal health."
        </p>
      </div>
    </div>
  );
}

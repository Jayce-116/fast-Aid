"use client";

import React from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";

const Navbar = () => {
  const pathname = usePathname();

  const getLinkClass = (path) => {
    const isActive = pathname === path;
    return isActive
      ? "text-green-600 font-semibold border-b-2 border-green-600"
      : "text-gray-700 hover:text-green-600 transition";
  };

  return (
    <nav className="w-full bg-white shadow-sm px-6 py-3 flex items-center justify-between fixed top-0 z-50">
      {/* Left side: Logo */}
      <div className="flex items-center space-x-2">
        <Link href="/" className="flex items-center space-x-2">
          <div className="w-10 h-10 rounded-full bg-green-600 text-white flex items-center justify-center font-bold">
            F.A
          </div>
          <div>
            <h1 className="text-xl font-bold text-green-600">FaST AID</h1>
            <p className="text-[10px] font-bold text-red-500 uppercase tracking-wider">Here for your safety</p>
          </div>
        </Link>
      </div>

      {/* Navigation Links */}
      <div className="hidden md:flex gap-8 items-center">
        <Link href="/" className={getLinkClass("/")}>
          Home
        </Link>

        <Link href="/dashboard" className={getLinkClass("/dashboard")}>
          Dashboard
        </Link>

        <Link href="/register" className={getLinkClass("/register")}>
          Register
        </Link>

        <Link href="/login" className={getLinkClass("/login")}>
          Login
        </Link>

        <button
          onClick={() => {
            localStorage.removeItem("token");
            localStorage.removeItem("username");
            window.location.href = "/login";
          }}
          className="bg-red-600 text-white px-4 py-2 rounded text-sm hover:bg-red-700 transition"
        >
          Logout
        </button>
      </div>
    </nav>
  );
};

export default Navbar;


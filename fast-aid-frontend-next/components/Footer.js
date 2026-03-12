import React from "react";

export default function Footer() {
  return (
    <footer className="bg-white py-6 mt-12 border-t">
      <div className="container mx-auto px-6 text-center text-gray-600">

        <div className="flex flex-col md:flex-row items-center justify-center gap-6 text-sm">

          <a href="#" className="hover:text-gray-800">
            Help Center
          </a>

          <a href="#" className="hover:text-gray-800">
            Jayce-116 ©
          </a>

          <a href="#" className="hover:text-gray-800">
            Privacy Policy
          </a>

          <a href="#" className="hover:text-gray-800">
            Terms of Service
          </a>

        </div>

        <p className="text-xs text-gray-400 mt-4">
          © {new Date().getFullYear()} FaST Aid — Built for East Africa
        </p>
      </div>
    </footer>
  );
}

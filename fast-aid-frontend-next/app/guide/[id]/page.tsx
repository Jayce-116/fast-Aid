"use client";

import React, { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import Link from "next/link";
import axios from "axios";

export default function GuideDetailsPage() {
  const params = useParams();
  const id = params?.id;
  const router = useRouter();
  const [guide, setGuide] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [currentStep, setCurrentStep] = useState(0);
  const [language, setLanguage] = useState("en");
  const [isListening, setIsListening] = useState(false);

  useEffect(() => {
    if (!id) return;
    
    axios
      .get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/guides/${id}`)
      .then((res) => {
        // Parse steps if they are stringified JSON
        const data = res.data;
        if (typeof data.steps === "string") {
          data.steps = JSON.parse(data.steps);
        }
        setGuide(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Guide fetch error:", err);
        setLoading(false);
      });
  }, [id]);

  const speak = (text: string) => {
    const speech = new SpeechSynthesisUtterance(text);
    const langMap: any = {
      en: "en-US",
      lg: "lg-UG",
      sw: "sw-KE",
      rn: "en-UG",
      ac: "en-UG",
    };
    speech.lang = langMap[language] || "en-US";
    speech.rate = 1;
    speech.pitch = 1;
    window.speechSynthesis.speak(speech);
  };

  const startVoiceAssistant = () => {
    const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
    if (!SpeechRecognition) {
      alert("Voice recognition not supported on this device.");
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.continuous = true;
    recognition.lang = "en-US";

    const translations: any = {
      en: { start: (title: string) => `Starting first aid guide for ${title}. Say Next to continue.`, next: "Next step", repeat: "Repeating the last step.", done: "You have finished all steps.", stop: "Voice assistant stopped." },
      lg: { start: (title: string) => `Ttandika obuyambi obusookerwako ku ${title}. Yogera nti Next oba Genda Mumaso.`, next: "Genda mu maaso.", repeat: "Nzikiriza okukyusa akadde kano.", done: "Osanze mu nteekateeka zonna.", stop: "Ebigambo bikuumiddwa." },
      sw: { start: (title: string) => `Kuanza mwongozo wa huduma ya kwanza kwa ${title}. Sema Next kuendelea.`, next: "Hatua inayofuata.", repeat: "Kurudia hatua ya mwisho.", done: "Umefika mwisho wa hatua zote.", stop: "Msaidizi wa sauti amesimamishwa." },
    };

    const trans = translations[language] || translations.en;
    speak(trans.start(guide.title));
    setIsListening(true);
    recognition.start();

    recognition.onresult = (event: any) => {
      const transcript = event.results[event.results.length - 1][0].transcript.trim().toLowerCase();
      console.log("User said:", transcript);

      if (transcript.includes("next")) {
        if (currentStep < guide.steps.length) {
          speak(guide.steps[currentStep]);
          setCurrentStep((prev) => prev + 1);
        } else {
          speak(trans.done);
        }
      } else if (transcript.includes("repeat")) {
        const stepIndex = currentStep - 1;
        if (stepIndex >= 0) speak(guide.steps[stepIndex]);
      } else if (transcript.includes("stop")) {
        window.speechSynthesis.cancel();
        recognition.stop();
        setIsListening(false);
        speak(trans.stop);
      }
    };

    recognition.onerror = () => setIsListening(false);
    recognition.onend = () => setIsListening(false);
  };

  if (loading) return (
    <div className="flex justify-center items-center min-h-[60vh]">
      <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-green-600"></div>
    </div>
  );

  if (!guide) return (
    <div className="container mx-auto px-6 py-20 text-center">
      <h2 className="text-3xl font-bold text-red-600 mb-4">Guide Not Found</h2>
      <Link href="/" className="text-green-600 font-bold hover:underline py-2 px-4 border-2 border-green-600 rounded-xl">
        Return Home
      </Link>
    </div>
  );

  return (
    <div className="container mx-auto px-6 py-12 max-w-4xl">
      <Link href="/" className="inline-flex items-center gap-2 text-green-700 font-semibold mb-8 hover:bg-green-50 px-4 py-2 rounded-xl transition">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m12 19-7-7 7-7"/><path d="M19 12H5"/></svg>
        Back to Library
      </Link>

      <div className="bg-white rounded-[2rem] shadow-xl overflow-hidden border border-gray-100">
        <div className="bg-green-600 p-8 md:p-12 text-white">
          <div className="flex flex-wrap items-center gap-4 mb-4">
             <span className="bg-white/20 px-4 py-1 rounded-full text-sm font-bold backdrop-blur-sm uppercase tracking-wider italic">
              {guide.category}
            </span>
            <div className="flex items-center gap-2 text-white/80 font-medium">
               <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
               {guide.estimated_time || "5 minutes"}
            </div>
          </div>
          <h1 className="text-4xl md:text-5xl font-extrabold tracking-tight mb-4">{guide.title}</h1>
          <p className="text-xl text-green-50 leading-relaxed font-medium opacity-90">{guide.summary}</p>
        </div>

        <div className="p-8 md:p-12">
          <div className="flex items-center justify-between mb-8">
            <h2 className="text-2xl font-bold text-gray-800 flex items-center gap-3">
              <span className="flex items-center justify-center w-8 h-8 bg-green-100 text-green-600 rounded-lg text-sm">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/></svg>
              </span>
              Step-by-Step Instructions
            </h2>
          </div>

          <div className="space-y-6">
            {guide.steps.map((step: string, index: number) => (
              <div key={index} className="flex gap-6 group">
                <div className="flex-shrink-0 w-10 h-10 rounded-2xl bg-gray-50 text-gray-400 font-bold flex items-center justify-center border border-gray-100 group-hover:bg-green-600 group-hover:text-white group-hover:border-green-600 transition-all">
                  {index + 1}
                </div>
                <div className="pt-2">
                  <p className="text-lg text-gray-700 leading-relaxed font-medium">{step}</p>
                </div>
              </div>
            ))}
          </div>

          <div className="mt-12 pt-12 border-t border-gray-100 flex flex-col md:flex-row items-center justify-between gap-8">
            <div className="flex flex-col gap-2">
              <label className="text-gray-500 text-sm font-bold uppercase tracking-widest">
                Voice Assistant Language
              </label>
              <select
                value={language}
                onChange={(e) => setLanguage(e.target.value)}
                className="bg-gray-50 border border-gray-200 px-6 py-3 rounded-2xl font-bold text-gray-700 focus:ring-2 focus:ring-green-200 outline-none appearance-none cursor-pointer hover:bg-white transition"
              >
                <option value="en">English</option>
                <option value="lg">Luganda</option>
                <option value="sw">Swahili</option>
                <option value="rn">Runyankole</option>
                <option value="ac">Acholi</option>
              </select>
            </div>

            <button
              onClick={startVoiceAssistant}
              disabled={isListening}
              className={`flex items-center gap-4 px-10 py-5 rounded-[1.5rem] font-extrabold text-xl shadow-2xl transition-all ${isListening ? "bg-red-100 text-red-600 cursor-not-allowed" : "bg-black text-white hover:bg-green-600 hover:scale-105 active:scale-95 shadow-black/10"}`}
            >
              <div className={`${isListening ? "animate-pulse" : ""}`}>
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="22"/></svg>
              </div>
              {isListening ? "Listening..." : "Start Voice Assistant"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

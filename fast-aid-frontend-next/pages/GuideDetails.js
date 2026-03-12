import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { ArrowLeft, Clock } from "lucide-react";
import axios from "axios";

const GuideDetails = () => {
  const { id } = useParams();
  const [guide, setGuide] = useState(null);
  const [loading, setLoading] = useState(true);

  // -------------------------------
  // 🔥 FETCH GUIDE FROM BACKEND
  // -------------------------------
  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/api/guides/${id}`)
      .then((res) => {
        setGuide(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Guide fetch error:", err);
        setLoading(false);
      });
  }, [id]);

  // -------------------------------
  // 🔥 VOICE ASSISTANT (your original code)
  // -------------------------------

  const [currentStep, setCurrentStep] = React.useState(0);
  const [language, setLanguage] = React.useState("en");

  const speak = (text) => {
    const speech = new SpeechSynthesisUtterance(text);

    const langMap = {
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

  const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;
  let recognition;

  if (SpeechRecognition) {
    recognition = new SpeechRecognition();
    recognition.continuous = true;
    recognition.lang = "en-US";
  }

  const translations = {
    en: {
      start: (title) =>
        `Starting first aid guide for ${title}. Say Next to continue.`,
      next: "Next step",
      repeat: "Repeating the last step.",
      done: "You have finished all steps.",
      stop: "Voice assistant stopped.",
    },
    lg: {
      start: (title) =>
        `Ttandika obuyambi obusookerwako ku ${title}. Yogera nti Next oba Genda Mumaso.`,
      next: "Genda mu maaso.",
      repeat: "Nzikiriza okukyusa akadde kano.",
      done: "Osanze mu nteekateeka zonna.",
      stop: "Ebigambo bikuumiddwa.",
    },
    sw: {
      start: (title) =>
        `Kuanza mwongozo wa huduma ya kwanza kwa ${title}. Sema Next kuendelea.`,
      next: "Hatua inayofuata.",
      repeat: "Kurudia hatua ya mwisho.",
      done: "Umefika mwisho wa hatua zote.",
      stop: "Msaidizi wa sauti amesimamishwa.",
    },
    rn: {
      start: (title) =>
        `Otandikire obuyambi obw'okubanza ku ${title}. Yogera nti Next oku genda mumaaso.`,
      next: "Genda mumaaso.",
      repeat: "Nzikiriza okuddamu ekitongole kino.",
      done: "Wazikiza ebyonna.",
      stop: "Eddoboozi lijjiddwa.",
    },
    ac: {
      start: (title) =>
        `Cak ame nyo kwede bedo kun guide pa ${title}. Mi ngec ka ni 'Next' me mede anyim.`,
      next: "Mede anyim.",
      repeat: "Doki cako kit ma dwogo.",
      done: "I tyeko kit weng.",
      stop: "Ki juko lobo me dwon.",
    },
  };

  const startVoiceAssistant = () => {
    if (!recognition) {
      alert("Voice recognition not supported on this device.");
      return;
    }

    speak(translations[language].start(guide.title));

    recognition.start();

    recognition.onresult = (event) => {
      const transcript = event.results[event.results.length - 1][0].transcript
        .trim()
        .toLowerCase();

      console.log("User said:", transcript);

      if (transcript.includes("next")) {
        if (currentStep < guide.steps.length) {
          speak(guide.steps[currentStep]);
          setCurrentStep((prev) => prev + 1);
        } else {
          speak(translations[language].done);
        }
      }

      if (transcript.includes("repeat")) {
        const stepIndex = currentStep - 1;
        if (stepIndex >= 0) speak(guide.steps[stepIndex]);
      }

      if (transcript.includes("start over")) {
        setCurrentStep(0);
        speak("Starting over.");
        speak(guide.steps[0]);
        setCurrentStep(1);
      }

      if (transcript.includes("stop")) {
        window.speechSynthesis.cancel();
        recognition.stop();
        speak(translations[language].stop);
      }
    };
  };

  // -------------------------------
  // 🔥 LOADING / NOT FOUND
  // -------------------------------
  if (loading) return <p className="p-6 text-center">Loading...</p>;
  if (!guide)
    return (
      <div className="p-6 text-center">
        <h2 className="text-2xl font-bold text-red-600">Guide Not Found</h2>
        <Link to="/" className="text-blue-600 underline">
          Return Home
        </Link>
      </div>
    );

  // -------------------------------
  // 🔥 RENDER GUIDE DETAILS
  // -------------------------------
  return (
    <div className="container mx-auto px-6 py-8">
      <Link to="/" className="flex items-center gap-2 text-blue-600 mb-6">
        <ArrowLeft size={20} /> Back to Home
      </Link>

      <h1 className="text-3xl font-bold mb-2">{guide.title}</h1>

      <p className="flex items-center text-gray-500 mb-6">
        <Clock size={18} className="mr-2" />
        Estimated time: {guide.estimated_time || "5 minutes"}
      </p>

      <div className="bg-white shadow-md rounded-xl p-6">
        <h2 className="text-xl font-semibold mb-4">Steps</h2>

        <ul className="list-decimal pl-6 space-y-3 text-gray-700">
          {guide.steps.map((step, index) => (
            <li key={index}>{step}</li>
          ))}
        </ul>

        <button
          onClick={startVoiceAssistant}
          className="bg-green-600 text-white px-4 py-2 rounded-lg shadow mt-6"
        >
          🎤 Start Voice Assistant
        </button>

        <div className="mt-4">
          <label className="text-gray-700 font-semibold">
            Select Language:
          </label>
          <select
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
            className="ml-3 border px-3 py-1 rounded"
          >
            <option value="en">English</option>
            <option value="lg">Luganda</option>
            <option value="sw">Swahili</option>
            <option value="rn">Runyankole</option>
            <option value="ac">Acholi</option>
          </select>
        </div>
      </div>
    </div>
  );
};

export default GuideDetails;

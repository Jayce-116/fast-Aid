// Save guides to localStorage
export const saveGuidesOffline = (guides) => {
  localStorage.setItem("offlineGuides", JSON.stringify(guides));
};

// Load guides from localStorage
export const loadGuidesOffline = () => {
  const data = localStorage.getItem("offlineGuides");
  return data ? JSON.parse(data) : null;
};

// Check if offline data exists
export const hasOfflineGuides = () => {
  return localStorage.getItem("offlineGuides") !== null;
};

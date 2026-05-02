import { create } from "zustand";

export const useLayoutStore = create((set) => ({
  currentTab: "",
  collapsedSidebar: true,
  toggleSidebar: () =>
    set((state) => ({ collapsedSidebar: !state.collapsedSidebar })),
  updateCurrentTab: (newTab: string) =>
    set((state) => ({ currentTab: newTab })),
}));

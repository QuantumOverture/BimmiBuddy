import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.tsx";
import { ClerkProvider } from "@clerk/react";
import { BrowserRouter } from "react-router";
import { ConfigProvider } from "antd";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <ConfigProvider>
      <ClerkProvider>
        <BrowserRouter>
          <App />
        </BrowserRouter>
      </ClerkProvider>
    </ConfigProvider>
  </StrictMode>,
);

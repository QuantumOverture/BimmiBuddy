import { Route, Routes } from "react-router";
import CoreLayout from "./components/Layout";

function App() {
  return (
    <Routes>
      <Route element={<CoreLayout />}>
        <Route index element={<p>Home</p>} />
        <Route path="planner" element={<p>Planner</p>} />
      </Route>
    </Routes>
  );
}

export default App;

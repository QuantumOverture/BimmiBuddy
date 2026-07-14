import { Route, Routes } from "react-router";
import CoreLayout from "./components/Layout";
import Planner from "./components/Planner";

function App() {
  return (
    <Routes>
      <Route element={<CoreLayout />}>
        <Route index element={<p>Home</p>} />
        <Route path="planner" element={<Planner/>} />
      </Route>
    </Routes>
  );
}

export default App;

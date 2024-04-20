import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider, Outlet } from "react-router-dom";
import Header from "./components/shared/Header";
import Footer from "./components/shared/Footer";
import Balance from "./pages/Balance";
function App() {
  const Layout = () => {
    return (
      <div className="flex flex-col">
        <Header />
        <div className="min-h-screen container">
          <Outlet />
        </div>
        <Footer />
      </div>
    );
  };
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Layout />,
      children: [
        {
          path: "/",
          element: <div>Home</div>,
        },
        {
          path: "/balance",
          element: <Balance />,
        },
      ],
    },
  ]);

  return createRoot(document.getElementById("root")).render(
    <RouterProvider router={router} />
  );
}

export default App;

import { Link } from "react-router-dom";

import GetYear from "./GetYear";

const Header = () => {
  return (
    <header className="bg-white max-h-22 pt-2 mb-5 pb-2 shadow-md">
      <div className="mx-auto flex justify-between h-16 max-w-screen-xl items-center gap-8 px-4 sm:px-6 lg:px-8">
        <div className="">
          <Link to="/">
            <a className="text-teal-600" href="#">
              <img src="src/assets/logo.png" alt="logo" className="h-[70px]" />
            </a>
          </Link>
        </div>

        <div className="flex items-center md:justify-between">
          <nav className="hidden md:block">
            <GetYear />
          </nav>
        </div>
        <div className="flex items-center gap-4">
          <div className="sm:flex sm:gap-4">
            <a
              className="block rounded-md bg-teal-600 px-5 py-2.5 text-sm font-medium text-white transition hover:bg-teal-700"
              href="#"
            >
              Login
            </a>

            <a
              className="hidden rounded-md bg-gray-100 px-5 py-2.5 text-sm font-medium text-teal-600 transition hover:text-teal-600/75 sm:block"
              href="#"
            >
              Register
            </a>
          </div>

          <button className="block rounded bg-gray-100 p-2.5 text-gray-600 transition hover:text-gray-600/75 md:hidden">
            <span className="sr-only">Toggle menu</span>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              strokeWidth="2"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M4 6h16M4 12h16M4 18h16"
              />
            </svg>
          </button>
        </div>
      </div>
    </header>
  );
};

export default Header;

import React, { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Link, useLocation } from 'react-router-dom'
import favicon from '../assets/favicon.png'
import { FaFacebook, FaWhatsapp, FaPhoneAlt, FaBars, FaTimes } from 'react-icons/fa'

const navItems = [
  { to: '/', label: 'Home' },
  { to: '/services', label: 'Services' },
  { to: '/blog', label: 'Blog' },
  { to: '/our-doctors', label: 'Our Doctors' },
  { to: '/about-us', label: 'About Us' },
  { to: '/contact-us', label: 'Contact Us' },
]

const Layout = ({ children }) => {
  const [menuOpen, setMenuOpen] = useState(false)
  const location = useLocation()

  useEffect(() => {
    setMenuOpen(false)
  }, [location])

  return (
    <div className="flex flex-col min-h-screen bg-gradient-to-br from-blue-50 via-white to-green-50 text-gray-800">
      <header className="fixed top-0 left-0 w-full bg-white bg-opacity-90 text-blue-900 shadow-lg z-50 backdrop-blur-md transition-all duration-300">
        <div className="container mx-auto flex justify-between items-center p-3">
          <Link to="/" className="text-1xl lg:text-2xl font-bold tracking-wide font-serif text-blue-800 hover:text-blue-600 transition-colors duration-300">
            <img src={favicon} alt="Surunga Medicine Center" className="w-10 h-10 inline-block mr-2" />
            Surunga Medicine Center
          </Link>

          <div className="lg:hidden">
            <button onClick={() => setMenuOpen(!menuOpen)} className="text-3xl focus:outline-none">
              {menuOpen ? <FaTimes /> : <FaBars />}
            </button>
          </div>

          <nav className="hidden lg:flex space-x-6">
            {navItems.map((link) => (
              <Link
                key={link.to}
                to={link.to}
                className="px-4 py-2 text-blue-800 font-medium hover:text-blue-600 transition duration-300 ease-in-out border-b-2 border-transparent hover:border-blue-600"
              >
                {link.label}
              </Link>
            ))}
            <Link
              to="/contact-us"
              className="px-6 py-2 text-white font-medium bg-green-500 rounded-full hover:bg-green-400 transition duration-300 ease-in-out transform hover:scale-105 shadow-md"
            >
              Book Appointment
            </Link>
          </nav>
        </div>
      </header>

      <AnimatePresence>
        {menuOpen && (
          <motion.nav
            initial={{ x: '100%' }}
            animate={{ x: 0 }}
            exit={{ x: '100%' }}
            transition={{ type: 'tween', duration: 0.3 }}
            className="lg:hidden fixed top-0 right-0 w-64 h-full bg-white shadow-2xl z-50 flex flex-col justify-start pt-20 px-6 space-y-4"
          >
            {navItems.map((link) => (
              <Link
                key={link.to}
                to={link.to}
                className="block px-4 py-2 text-blue-800 font-medium hover:text-blue-600 transition duration-300 ease-in-out border-b border-gray-200"
                onClick={() => setMenuOpen(false)}
              >
                {link.label}
              </Link>
            ))}
            <Link
              to="/request-call"
              className="block px-4 py-2 text-white font-medium bg-green-500 rounded-md hover:bg-green-400 transition duration-300 ease-in-out text-center mt-4"
              onClick={() => setMenuOpen(false)}
            >
              Book Appointment
            </Link>
          </motion.nav>
        )}
      </AnimatePresence>

      <main className="flex-grow container mx-auto pt-24 pb-12 px-6">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -20 }}
          transition={{ duration: 0.3 }}
        >
          {children}
        </motion.div>
      </main>

      <footer className="bg-blue-800 text-white py-6">
        <div className="container mx-auto px-6">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
            <div className="space-y-3">
              <h3 className="text-2xl font-semibold">Surunga Medicine Center</h3>
              <p className="text-blue-200">Providing quality healthcare services since 2000</p>
            </div>
            <div className="space-y-2">
              <h4 className="text-xl font-semibold">Quick Links</h4>
              <ul className="space-y-1">
                {[
                  { href: '/', label: 'Privacy Policy' },
                  { href: '/services', label: 'Terms of Service' },
                  { href: '/contact-us', label: 'Contact Us' },
                ].map((link) => (
                  <li key={link.href}>
                    <a
                      href={link.href}
                      className="text-blue-200 hover:text-white transition duration-300 ease-in-out"
                    >
                      {link.label}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
            <div className="space-y-2">
              <h4 className="text-xl font-semibold">Connect With Us</h4>
              <div className="flex space-x-4">
                <a href="https://www.facebook.com/surungamedicine" className="text-blue-200 hover:text-white transition duration-300 ease-in-out text-2xl">
                  <FaFacebook /> 
                </a>
                <a href="https://wa.me/9804964107" target='_blank' className="text-blue-200 hover:text-white transition duration-300 ease-in-out text-2xl">
                  <FaWhatsapp />
                </a>
                <a href="tel:023-553097" className="text-blue-200 hover:text-white transition duration-300 ease-in-out text-2xl">
                  <FaPhoneAlt />
                </a>
              </div>
            </div>
          </div>
          <div className="mt-3 pt-3 border-t border-blue-800 text-center">
            <p className="text-blue-200">&copy; {new Date().getFullYear()} Surunga Medicine Center. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}

export default Layout


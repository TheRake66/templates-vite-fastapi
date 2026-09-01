/**
 * Nom du module         : main.tsx
 * Description           : 
 *   Point d'entrée de l'application, contient les routes et
 *   les imports principaux.
 * 
 * Auteur                : TheRake66
 * Date de création      : 2026-08-28 04:01:51
 * Dernière modification : 2026-08-28 04:01:51
 * Version               : 1.0.0
 * Licence               : GPL-3.0
 * 
 * Notes                 : 
 */

import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { Navigate } from 'react-router-dom';
import { HelmetProvider } from 'react-helmet-async';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import { initTheme } from './libraries/theme.ts';
import { initFullscreen } from './libraries/fullscreen.ts';
import { initLanguage } from './libraries/language.ts';
import { initAnalytics, AnalyticsTracker } from './libraries/analytics.ts';

/**
 * Injection des fichiers de style.
 */
import './font.scss';
import './theme.scss';
import './variable.scss';
import './global.scss';

/**
 * Initialisation des librairies.
 */
initTheme();
initFullscreen();
initLanguage();
initAnalytics();

/**
 * Définition des routes vers les pages.
 */
createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <HelmetProvider>
      <Router>
        <AnalyticsTracker />
        <Routes>
          
          <Route path="/" element={<Navigate to="/" replace />} />
          
          
          
          <Route path="*" element={<Navigate to="/" replace />} />
          
        </Routes>
      </Router>
    </HelmetProvider>
  </StrictMode>
);
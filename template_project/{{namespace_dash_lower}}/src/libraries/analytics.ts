/**
 * Nom du module         : analytics.ts
 * Description           : 
 *   Gère automatiquement l'enregistrement de chaque changement
 *   de page auprès du service Google Analytics.
 * 
 * Auteur                : TheRake66
 * Date de création      : 2026-08-28 04:01:51
 * Dernière modification : 2026-08-28 04:01:51
 * Version               : 1.0.0
 * Licence               : GPL-3.0
 * 
 * Notes                 : 
 */

import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import ReactGA from 'react-ga4';
import config from '../react.json';

/**
 * Initialise l'état de la librairie Google Analytics avec le Google ID
 * présent dans le fichier de configuration de l'application.
 */
export function initAnalytics(): void {
  ReactGA.initialize(config.analytics.googleid);
}

/**
 * Composant React qui écoute les changements de localisation du routeur
 * et envoie un événement de type 'pageview' à Google Analytics.
 * 
 * @returns {null} Ce composant n'affiche aucun élément visuel.
 */
export function AnalyticsTracker(): null {
  const location = useLocation();
  useEffect(() => {
    ReactGA.send({ 
      hitType: 'pageview', 
      page: location.pathname + location.search 
    });
  }, [location]);
  return null;
}
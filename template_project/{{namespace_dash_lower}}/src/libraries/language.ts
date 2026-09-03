/**
 * Nom du module         : language.ts
 * Description           : Gère le système d'internationalisation.
 * 
 * Auteur                : TheRake66
 * Date de création      : 2026-08-28 04:01:51
 * Dernière modification : 2026-08-28 04:01:51
 * Version               : 1.0.0
 * Licence               : GPL-3.0
 * 
 * Notes                 : 
 */

import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';
import resourcesToBackend from 'i18next-resources-to-backend';
import config from '../react.json';
import type { LanguageType } from '../enums/language.type.ts';

const defaultLang = config.default.language;
const storageKey = config.localstorage.language;

/**
 * Initialise le système d'internationalisation (i18n) avec
 * les traduction chargées.
 */
export function initLanguage(): void {
  const language = getLanguage();
  i18n
    .use(LanguageDetector)
    .use(initReactI18next)
    .use(resourcesToBackend((language: string, namespace: string) => 
      import(`../locales/${language}/${namespace}.json`)))
    .init({
      lng: language,
      fallbackLng: defaultLang,
      ns: ['pages', 'components'],
      interpolation: { escapeValue: false }});
}

/**
 * Modifie la langue active de l'application.
 * 
 * @param {LanguageType} language Le code de la nouvelle langue à appliquer.
 */
export function setLanguage(language: LanguageType): void {
  i18n.changeLanguage(language);
  localStorage.setItem(storageKey, language);
}

/**
 * Récupère la langue actuellement de l'application.
 * 
 * @returns {LanguageType} La langue actuellement utilisée.
 */
export function getLanguage(): LanguageType {
  const stored = localStorage.getItem(storageKey) ?? defaultLang;
  return stored as LanguageType;
}
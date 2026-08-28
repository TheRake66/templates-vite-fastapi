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
import configuration from '../configuration.json';
import type { LanguageType } from '../enums/language.type.ts';

import {{language_short}} from '../locales/{{language_short}}.json';

const defaultLang = configuration.default.language;
const storageKey = configuration.localstorage.language;

/**
 * Initialise le système d'internationalisation (i18n) avec
 * les traduction chargées.
 */
export function initLanguage(): void {
  const language = getLanguage();
  i18n
    .use(LanguageDetector)
    .use(initReactI18next)
    .init({
      lng: language,
      fallbackLng: defaultLang,
      interpolation: { escapeValue: false },
      resources: {
        {{language_short}}: { translation: {{language_short}} }
      }});
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
/**
 * Nom du module         : theme.ts
 * Description           : Gère le thème des couleurs.
 * 
 * Auteur                : TheRake66
 * Date de création      : 2026-08-28 04:01:51
 * Dernière modification : 2026-08-28 04:01:51
 * Version               : 1.0.0
 * Licence               : GPL-3.0
 * 
 * Notes                 : 
 */

import configuration from '../react.json';
import type { ThemeType } from '../enums/theme.type.ts';

const defaultTheme = configuration.default.theme;
const storageKey = configuration.storage.theme;

/**
 * Initialise le thème des couleurs en récupérant la valeur enregistrée 
 * ou celle défaut dans le fichier de configuration de l'application.
 */
export function initTheme(): void {
  const theme = getTheme();
  document.body.setAttribute('data-theme', theme);
}

/**
 * Modifie le thème actif des couleurs .
 * 
 * @param {ThemeType} theme Le nouveau thème à appliquer.
 */
export function setTheme(theme: ThemeType): void {
  document.body.setAttribute('data-theme', theme);
  localStorage.setItem(storageKey, theme);
}

/**
 * Récupère le thème actif des couleurs.
 * 
 * @returns {ThemeType} Le thème actif des couleur.
 */
export function getTheme(): ThemeType {
  const stored = localStorage.getItem(storageKey) ?? defaultTheme;
  return stored as ThemeType;
}
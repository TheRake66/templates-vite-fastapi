/**
 * Nom du module         : theme.type.ts
 * Description           : Énumération des thèmes de couleurs.
 * 
 * Auteur                : TheRake66
 * Date de création      : 2026-08-28 04:01:51
 * Dernière modification : 2026-08-28 04:01:51
 * Version               : 1.0.0
 * Licence               : GPL-3.0
 * 
 * Notes                 : 
 */

/**
 * Liste d'énumération Theme.
 */
export const Theme = {
  Dark: 'dark',
  Light: 'light'
} as const;

/**
 * Conversion en type ThemeType.
 */
export type ThemeType = typeof Theme[keyof typeof Theme];
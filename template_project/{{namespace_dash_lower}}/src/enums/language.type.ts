/**
 * Nom du module         : language.type.ts
 * Description           : Énumération des langues pour i18n.
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
 * Liste d'énumération Language.
 */
export const Language = {
  {{language_name}}: '{{language_short}}'
} as const;

/**
 * Conversion en type LanguageType.
 */
export type LanguageType = typeof Language[keyof typeof Language];
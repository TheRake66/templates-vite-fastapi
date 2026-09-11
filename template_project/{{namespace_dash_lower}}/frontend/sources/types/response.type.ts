/**
 * Nom du module         : response.type.ts
 * Description           : Structure des données des réponses du back-end.
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
 * Définition du type Response.
 */
export interface Response<T = unknown> {
  message: string;
  code: number;
  content: T;
}
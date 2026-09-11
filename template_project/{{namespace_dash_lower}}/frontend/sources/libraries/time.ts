/**
 * Nom du module         : time.ts
 * Description           : Gère le format de temps.
 * 
 * Auteur                : TheRake66
 * Date de création      : 2026-08-28 04:01:51
 * Dernière modification : 2026-08-28 04:01:51
 * Version               : 1.0.0
 * Licence               : GPL-3.0
 * 
 * Notes                 : 
 */

import type { TimeType } from '../types/time.type.ts';

/**
 * Convertit un nombre total de secondes en une structure de temps découpée 
 * en heures, minutes et secondes.
 * 
 * @param {number} time Le nombre de secondes à convertir.
 * @returns {TimeType} Un objet contenant les heures, minutes et secondes.
 */
export function parseTime(time: number): TimeType {
  const total = Math.floor(time);
  const hours = Math.floor(total / 3600);
  const minutes = Math.floor((total % 3600) / 60);
  const seconds = total % 60;
  return { hours, minutes, seconds };
}

/**
 * Formate un objet ou un nombre de secondes en une chaîne de caractères
 * au format HH:MM:SS avec un zéro initial si nécessaire.
 * 
 * @param {TimeType | number} value Un objet ou un nombre de secondes brut.
 * @returns {string} Le temps formaté sous la forme "HH:MM:SS".
 */
export function formatTime(time: TimeType): string;
export function formatTime(seconds: number): string;
export function formatTime(value: TimeType | number): string {
  const time = typeof value === 'number' ? parseTime(value) : value;
  const pad = (value: number): string => value.toString().padStart(2, '0');
  return `${pad(time.hours)}:${pad(time.minutes)}:${pad(time.seconds)}`;
}
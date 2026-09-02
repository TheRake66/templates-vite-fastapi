/**
 * Nom du module         : api.ts
 * Description           : Gère la connexion avec l'API.
 * 
 * Auteur                : TheRake66
 * Date de création      : 2026-08-28 04:01:51
 * Dernière modification : 2026-08-28 04:01:51
 * Version               : 1.0.0
 * Licence               : GPL-3.0
 * 
 * Notes                 : 
 */

import axios from 'axios';
import configuration from '../configuration.json';

const conf = configuration.api;
const prot = conf.ssl ? 'https' : 'http';

/**
 * Objet contenant la connexion à l'API.
 */
const api = axios.create({
  baseURL: `${prot}://${conf.server}:${conf.port}/api/${conf.version}/`,
  headers: { 'Content-Type': 'application/json' },
  timeout: 10000
});

/**
 * Export de l'objet en tant que service.
 */
export default api;
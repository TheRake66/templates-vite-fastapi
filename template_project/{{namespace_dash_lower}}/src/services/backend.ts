/**
 * Nom du module         : backend.ts
 * Description           : Gère la connexion avec le serveur de données.
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
import { io, Socket } from 'socket.io-client';
import config from '../react.json';

interface BackConfig {
  address: string;
  port: number;
  version: string;
  wspath: string;
  ssl: boolean;
  timeout: number;
}

const backend: BackConfig = config.backend;
const protocol: string = backend.ssl ? 'https' : 'http';

/**
 * Objet contenant la connexion à l'API REST.
 */
export const rest = axios.create({
  baseURL: `${protocol}://${backend.address}:${backend.port}/api/${backend.version}/`,
  headers: { 'Content-Type': 'application/json' },
  timeout: backend.timeout
});

/**
 * Objet contenant la connexion au WebSocket.
 */
export const socket: Socket = io(`${protocol}://${backend.address}:${backend.port}`, {
  autoConnect: true,
  transports: [ 'websocket', 'polling' ],
  timeout: backend.timeout,
  path: backend.wspath,
});
import { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { useNavigate, useParams } from "react-router-dom";
import styles from './{{lower_name}}.module.scss';

interface {{title_name}}Props {
  
}

export default function {{title_name}}({}: {{title_name}}Props) {
  const { t, i18n } = useTranslation('', { keyPrefix: 'pages.{{namespace_dots_lower}}' });
  const navigate = useNavigate();
  const { } = useParams();

  const [value, setValue] = useState('');

  const mount = () => {
    
  };

  const unmount = () => {
    
  };

  useEffect(() => {
    mount();
    return unmount;
  });

  return (
    <main className={styles.container}>
      Bienvenue sur la page {{title_name}} !
    </main>
  );
}
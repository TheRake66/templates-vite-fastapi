import { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { useNavigate, useParams } from "react-router-dom";
import styles from './{{lower_name}}.module.scss';

interface {{title_name}}Props {
  
}

export default function {{title_name}}({}: {{title_name}}Props) {
  const { t, i18n } = useTranslation('', { keyPrefix: 'components.{{namespace_dots_lower}}' });
  const navigate = useNavigate();
  const { } = useParams();

  const [value, setValue] = useState('');

  useEffect(() => {
    
  }, []);

  return (
    <div className={styles.container}>
      Bonjour le composant {{title_name}} !
    </div>
  );
}
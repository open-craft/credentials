import React from 'react';
import ReactDOM from 'react-dom';

import CredentialList from './CredentialList';

function CredentialListFactory(parent, props) {
  const formattedProps = {
    programCerts: props.programCerts,
    username: props.username,
    lmsBaseUrl: props.lmsBaseUrl,
    recordsPrograms: props.recordsPrograms,
    // ...props.record,
    // isPublic: props.isPublic,
    // icons: props.icons,
    // uuid: props.uuid,
    // helpUrl: props.helpUrl,
    // programListUrl: props.programListUrl,
  };

  ReactDOM.render(
    React.createElement(CredentialList, { ...formattedProps }, null),
    document.getElementById(parent),
  );
}

export { CredentialListFactory }; // eslint-disable-line import/prefer-default-export

import React from 'react';
import axios from 'axios';
import PropTypes from 'prop-types';
import { Button, Icon, StatusAlert } from '@edx/paragon';
import Cookies from 'js-cookie';

import FoldingTable from './FoldingTable';
import RecordsHelp from './RecordsHelp';
import ProgramIcon from './ProgramIcon';
import SendLearnerRecordModal from './SendLearnerRecordModal';
import ShareProgramRecordModal from './ShareProgramRecordModal';
import StringUtils from './Utils';
import trackEvent from './Analytics';

class CredentialList extends React.Component {
  constructor(props) {
    super(props);
    this.username = props.username;
    this.lmsBaseUrl = props.lmsBaseUrl,
    this.courseCerts = []
    this.handleCourseCertData = this.handleCourseCertData.bind(this);
    this.state = {
      courseCerts: [],
      programCerts: props.programCerts,
      recordsPrograms: props.recordsPrograms,
    };
    console.log(this.state.recordsPrograms);
  }

  componentDidMount() {
      this.getCourseCerts();
  }

  componentDidUpdate() {
  }

  handleCourseCertData(request) {
    this.setState({
      courseCerts: request.data,
    });
  }

  getCourseCertApiUrl() {
      return `${this.lmsBaseUrl}/api/certificates/v0/certificates/${this.username}/`
  }

  getCourseCerts() {
    const headers = {
      withCredentials: true,
      headers: {
      },
    };

    axios.get(this.getCourseCertApiUrl(), headers)
        .then(this.handleCourseCertData)
        .catch(data => console.log(data))
  }

  render() {
    return (
      <main id="main-content" style={{"max-width": "1200px", "margin": "auto"}} tabIndex="-1">
        <h2>Download your certificates</h2>
        <div style={{
            "height": "300px",
            "width": "800px",
            "background-color": "black",
            "text-align": "center",
            "display": "flex",
            "align-items": "center",
            "justify-content": "center",
            "font-size": "30px",
            "color": "white",
        }}>
            Video
        </div>
        <h3>Download Course Certs</h3>
        <ul>
          {this.state.courseCerts.map(cert => (<li><a href="{cert.download_url}">{cert.course_display_name}</a></li>))}
        </ul>
        <h3>Download Program Certs</h3>
        <ul>
          {this.state.programCerts.map(cert => (<li><a href="{cert.certificate_url}">{cert.program_title}</a></li>))}
        </ul>
        <h3>Download Program Records</h3>
        <ul>
          {this.state.recordsPrograms.map(recordProgram => (<li><a href={`/records/programs/${recordProgram.uuid}`}>{recordProgram.name} | {recordProgram.partner} </a></li>))}
        </ul>
      </main>
    );
  }
}

CredentialList.propTypes = {
};

CredentialList.defaultProps = {
};

export default CredentialList;

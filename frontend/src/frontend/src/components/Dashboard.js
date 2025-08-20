import React from 'react';
import LogUploader from './LogUploader';
import PredictionResults from './PredictionResults';

const Dashboard = () => {
  return (
    <div className="dashboard">
      <h1>AI DevOps Predictor Dashboard</h1>
      <LogUploader />
      <PredictionResults />
    </div>
  );
};

export default Dashboard;

import React, { useEffect, useState } from "react";
import { getTweetIdeas, getLeads } from "../service/api";
import { FaUsers, FaMousePointer, FaCheckCircle, FaEnvelope, FaLightbulb } from "react-icons/fa";

const Dashboard = () => {
  const [tweetIdeas, setTweetIdeas] = useState([]);
  const [leads, setLeads] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const ideas = await getTweetIdeas();
      setTweetIdeas(ideas);

      const leadsData = await getLeads();
      setLeads(leadsData);
    }
    fetchData();
  }, []);

  const totalLeads = leads.length;
  const clickedLeads = leads.filter((lead) => lead.clicked).length;
  const convertedLeads = leads.filter((lead) => lead.converted).length;

  const ctr = totalLeads > 0 ? ((clickedLeads / totalLeads) * 100).toFixed(1) : 0;
  const conversionRate = totalLeads > 0 ? ((convertedLeads / totalLeads) * 100).toFixed(1) : 0;

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 to-blue-50 p-8">
      {/* Header */}
      <header className="text-center mb-12">
        <h1 className="text-5xl font-extrabold text-gray-800 mb-2">Agent 2 Dashboard</h1>
        <p className="text-gray-600 text-lg">Suivi des idées de tweets et des leads générés</p>
      </header>

      {/* Section Idées de Tweets */}
      <div className="bg-gradient-to-r from-indigo-100 to-purple-100 shadow-lg rounded-2xl p-6 mb-10">
        <div className="flex items-center mb-4">
          <FaLightbulb className="text-yellow-500 text-3xl mr-3" />
          <h2 className="text-2xl font-bold text-gray-800">Idées de Tweets Générées</h2>
        </div>
        {tweetIdeas.length === 0 ? (
          <p className="text-gray-500">Aucune idée générée pour le moment.</p>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full table-auto border-collapse">
              <thead>
                <tr className="bg-indigo-200 text-indigo-800">
                  <th className="border px-4 py-2 text-left">Contenu du Tweet</th>
                </tr>
              </thead>
              <tbody>
                {tweetIdeas.map((idea, idx) => (
                  <tr key={idx} className="hover:bg-indigo-50 transition-colors">
                    <td className="border px-4 py-2">{idea.content}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {/* Section Leads Contactés */}
      <div className="bg-gradient-to-r from-green-100 to-teal-100 shadow-lg rounded-2xl p-6 mb-10">
        <div className="flex items-center mb-4">
          <FaEnvelope className="text-green-600 text-3xl mr-3" />
          <h2 className="text-2xl font-bold text-gray-800">Leads Contactés</h2>
        </div>
        {leads.length === 0 ? (
          <p className="text-gray-500">Aucun lead contacté pour le moment.</p>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full table-auto border-collapse">
              <thead>
                <tr className="bg-green-200 text-green-800">
                  <th className="border px-4 py-2 text-left">Nom</th>
                  <th className="border px-4 py-2 text-left">Twitter</th>
                  <th className="border px-4 py-2 text-left">Message envoyé</th>
                  <th className="border px-4 py-2 text-left">Réponse</th>
                </tr>
              </thead>
              <tbody>
                {leads.map((lead) => (
                  <tr key={lead.id} className="hover:bg-green-50 transition-colors">
                    <td className="border px-4 py-2">{lead.name}</td>
                    <td className="border px-4 py-2">{lead.twitter_handle}</td>
                    <td className="border px-4 py-2">{lead.message_sent}</td>
                    <td className="border px-4 py-2">{lead.response || "Pas encore de réponse"}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {/* Statistiques */}
      <div className="bg-gradient-to-r from-yellow-100 to-orange-100 shadow-lg rounded-2xl p-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center gap-3">
          📊 Statistiques
        </h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
          <div className="bg-white p-5 rounded-xl shadow flex flex-col items-center">
            <FaUsers className="text-4xl text-blue-500 mb-2" />
            <p className="text-sm font-medium text-gray-600">Leads Totaux</p>
            <p className="text-2xl font-bold">{totalLeads}</p>
          </div>
          <div className="bg-white p-5 rounded-xl shadow flex flex-col items-center">
            <FaMousePointer className="text-4xl text-green-500 mb-2" />
            <p className="text-sm font-medium text-gray-600">CTR</p>
            <p className="text-2xl font-bold">{ctr}%</p>
          </div>
          <div className="bg-white p-5 rounded-xl shadow flex flex-col items-center">
            <FaCheckCircle className="text-4xl text-purple-500 mb-2" />
            <p className="text-sm font-medium text-gray-600">Conversions</p>
            <p className="text-2xl font-bold">{conversionRate}%</p>
          </div>
          <div className="bg-white p-5 rounded-xl shadow flex flex-col items-center">
            <FaEnvelope className="text-4xl text-yellow-500 mb-2" />
            <p className="text-sm font-medium text-gray-600">Leads Cliqués</p>
            <p className="text-2xl font-bold">{clickedLeads}</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;

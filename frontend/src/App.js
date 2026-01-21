import TweetIdeasTable from "./components/TweetIdeasTable";

const App = () => {
  return (
    <div className="min-h-screen bg-gray-50 p-6">
      {/* Titre du dashboard */}
      <header className="mb-8 text-center">
        <h1 className="text-4xl font-bold text-gray-800 mb-2">Dashboard Agent 2</h1>
        <p className="text-gray-500 text-lg">
          Suivi des idées de tweets générées et leads contactés
        </p>
      </header>

      {/* Carte contenant le composant TweetIdeasTable */}
      <div className="bg-white shadow-lg rounded-xl p-6 max-w-5xl mx-auto">
        <TweetIdeasTable />
      </div>
    </div>
  );
};

export default App;

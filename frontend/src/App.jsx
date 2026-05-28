import { useEffect, useState } from "react";
import api from "./api/api";

function App() {

  const [records, setRecords] = useState([]);

  const [selectedFile, setSelectedFile] = useState(null);

  const [message, setMessage] = useState("");

  useEffect(() => {
    fetchRecords();
  }, []);

  const fetchRecords = async () => {

    try {

      const response = await api.get("records/");

      setRecords(response.data);

    } catch (error) {

      console.error(error);

    }
  };

  const handleFileChange = (event) => {

    setSelectedFile(event.target.files[0]);

  };

  const handleUpload = async () => {

    if (!selectedFile) {

      alert("Please select a CSV file");

      return;
    }

    const formData = new FormData();

    formData.append("file", selectedFile);

    try {

      await api.post(
        "upload/sap/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setMessage("SAP CSV uploaded successfully");

      fetchRecords();

    } catch (error) {

      console.error(error);

      setMessage("Upload failed");

    }
  };

  const totalRecords = records.length;

  const suspiciousRecords = records.filter(
    (record) => record.suspicious
  ).length;

  const approvedRecords = records.filter(
    (record) => record.status === "approved"
  ).length;

  const totalCO2e = records.reduce(
    (sum, record) => sum + (record.co2e || 0),
    0
  );

  return (

    <div style={{ padding: "30px" }}>

      <h1>CarbonLedger Dashboard</h1>

      <div style={{ marginBottom: "20px" }}>

        <input
          type="file"
          onChange={handleFileChange}
        />

        <button
          onClick={handleUpload}
          style={{
            marginLeft: "10px",
            padding: "6px 14px",
            cursor: "pointer"
          }}
        >
          Upload SAP CSV
        </button>

      </div>

      <p>{message}</p>

      <div
        style={{
          display: "flex",
          gap: "20px",
          marginBottom: "30px",
          flexWrap: "wrap"
        }}
      >

        <div style={cardStyle}>
          <h3>Total Records</h3>
          <p>{totalRecords}</p>
        </div>

        <div style={cardStyle}>
          <h3>Suspicious Records</h3>
          <p>{suspiciousRecords}</p>
        </div>

        <div style={cardStyle}>
          <h3>Approved Records</h3>
          <p>{approvedRecords}</p>
        </div>

        <div style={cardStyle}>
          <h3>Total CO2e</h3>
          <p>{totalCO2e.toFixed(2)}</p>
        </div>

      </div>

      <table border="1" cellPadding="10">

        <thead>

          <tr>

            <th>ID</th>
            <th>Category</th>
            <th>Quantity</th>
            <th>Unit</th>
            <th>CO2e</th>
            <th>Suspicious</th>
            <th>Status</th>

          </tr>

        </thead>

        <tbody>

          {records.map((record) => (

            <tr key={record.id}>

              <td>{record.id}</td>

              <td>{record.category}</td>

              <td>{record.quantity}</td>

              <td>{record.unit}</td>

              <td>{record.co2e}</td>

              <td>
                {record.suspicious ? "⚠️ Yes" : "No"}
              </td>

              <td>{record.status}</td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>

  );
}

const cardStyle = {
  border: "1px solid #ccc",
  padding: "20px",
  borderRadius: "10px",
  minWidth: "180px",
  boxShadow: "0px 2px 6px rgba(0,0,0,0.1)"
};

export default App;
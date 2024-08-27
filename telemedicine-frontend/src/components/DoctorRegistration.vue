<template>
  <div class="doctor-registration">
    <h2>Doctor Registration</h2>
    <form @submit.prevent="registerDoctor">
      <div class="form-group">
        <label for="name">Name:</label>
        <input id="name" v-model="doctor.name" type="text" required>
      </div>

      <div class="form-group">
        <label for="gender">Gender:</label>
        <select id="gender" v-model="doctor.gender" required>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>
      </div>

      <div class="form-group">
        <label for="email">Email:</label>
        <input id="email" v-model="doctor.email" type="email" required>
      </div>

      <div class="form-group">
        <label for="phone">Phone:</label>
        <input id="phone" v-model="doctor.phone" type="tel" required>
      </div>

      <div class="form-group">
        <label for="address_line">Address:</label>
        <input id="address_line" v-model="doctor.address_line" type="text" required>
      </div>

      <div class="form-group">
        <label for="city">City:</label>
        <input id="city" v-model="doctor.city" type="text" required>
      </div>

      <div class="form-group">
        <label for="state">State:</label>
        <input id="state" v-model="doctor.state" type="text" required>
      </div>

      <div class="form-group">
        <label for="country">Country:</label>
        <input id="country" v-model="doctor.country" type="text" required>
      </div>

      <div class="form-group">
        <label for="postal_code">Postal Code:</label>
        <input id="postal_code" v-model="doctor.postal_code" type="text" required>
      </div>

      <div class="form-group">
        <label for="description">Profile Description:</label>
        <textarea id="description" v-model="doctor.description"></textarea>
      </div>

      <div class="form-group">
        <label for="experience_years">Years of Experience:</label>
        <input id="experience_years" v-model.number="doctor.experience_years" type="number" required>
      </div>

      <div class="form-group">
        <label for="qualifications">Qualifications:</label>
        <textarea id="qualifications" v-model="doctor.qualifications"></textarea>
      </div>

      <div class="form-group">
        <label for="specialties">Specialties:</label>
        <textarea id="specialties" v-model="doctor.specialties"></textarea>
      </div>

      <button type="submit">Register</button>
    </form>

    <div v-if="message" :class="['message', messageType]">
      {{ message }}
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'DoctorRegistration',
  data() {
    return {
      doctor: {
        identifier: '', // You might want to generate this or get it from somewhere
        name: '',
        gender: '',
        email: '',
        phone: '',
        address_line: '',
        city: '',
        state: '',
        country: '',
        postal_code: '',
        description: '',
        experience_years: null,
        qualifications: '',
        specialties: '',
        profile_picture: null // You can add file upload for this later
      },
      message: '',
      messageType: ''
    }
  },
  methods: {
    async registerDoctor() {
      try {
        const response = await axios.post('/api/doctor/register', this.doctor);
        this.message = 'Registration successful!';
        this.messageType = 'success';
        console.log('Doctor registered:', response.data);
        // You might want to redirect the user or clear the form here
      } catch (error) {
        this.message = error.response.data.error || 'An error occurred during registration.';
        this.messageType = 'error';
        console.error('Registration error:', error.response.data);
      }
    }
  }
}
</script>

<style scoped>
.doctor-registration {
  max-width: 500px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input, select, textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

.message {
  margin-top: 15px;
  padding: 10px;
  border-radius: 4px;
}

.success {
  background-color: #d4edda;
  color: #155724;
}

.error {
  background-color: #f8d7da;
  color: #721c24;
}
</style>
